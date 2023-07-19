from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND, 
    HTTP_409_CONFLICT, 
    HTTP_413_REQUEST_ENTITY_TOO_LARGE
)

from apps.testing.models import Question, Subject, Variation, TestResultModel
from apps.testing.serializers import (
    TestSerializer,
    SubjectSerializer,
    QuestionSerializer,
    VariationSerializer
)


def home(request):
    return HttpResponse("[INFO] Application started successfully")



class VariationCreateAPIView(CreateAPIView):
    model = Variation
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()
    # permission_classes = [IsAdminUser]

    def get_object(self, question_id):
        query = self.queryset.filter(question_id=question_id)
        return (query, query.count() < 4)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_id = serializer.validated_data.get("question_id")

        # Check if the maximum variation limit is reached
        if not self.get_object(question_id)[-1]:
            return Response(
                data={"msg": f"Max variation limit for question {question_id} exceeded!"},
                status=HTTP_413_REQUEST_ENTITY_TOO_LARGE
            )

        # Check if it is the last variation
        if self.get_object(question_id)[0].count() == 3:
            if not serializer.validated_data.get("is_correct"):
                return Response(
                    data={
                        "msg": "Question has no correct variations, and this is the last variation. "
                               "You must either mark it as correct or update another correct variation."
                    },
                    status=HTTP_400_BAD_REQUEST
                )

        # Check if the variation being created has is_correct set to true
        if serializer.validated_data.get("is_correct"):
            variations = self.get_object(question_id)[0]
            if variations.filter(is_correct=True).exists():
                return Response(
                    data={"msg": "There is already a correct answer for this question. Set the current "
                                  "variation as incorrect instead."},
                    status=HTTP_409_CONFLICT
                )

        return super().post(request, *args, **kwargs)

class QuestionsCreateAPIView(CreateAPIView):
    model = Question
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    # permission_classes = [IsAdminUser]

    def get_object(self):
        subject_id = self.request.POST.get("subject_id")
        if subject_id:
            query = self.queryset.filter(subject_id=subject_id).count()
            return query < 4
        else:
            return Response(
                data={
                    "msg": "Please provide subject id"
                },
                status=HTTP_400_BAD_REQUEST
            )

    def post(self, request, *args, **kwargs):
        if self.get_object():
            return super().post(request, *args, **kwargs)
        else:
            return Response(
                data={
                    "msg": f"Max question limit for subject id: {self.request.POST.get('subject_id')} exceeded!"
                },
                status=HTTP_413_REQUEST_ENTITY_TOO_LARGE
            )

class SubjectCreateAPIView(CreateAPIView):
    model = Subject
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    # permission_classes = [IsAdminUser]

class TestResultCreateAPIView(CreateAPIView):
    model = TestResultModel
    queryset = TestResultModel.objects.all()
    serializer_class = TestSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        questions = serializer.validated_data.get("questions")  # type: ignore
        subject_id = serializer.validated_data.get("subject_id")  # type: ignore
        subject = Question.objects.filter(subject_id=subject_id)
        score = 0
        # counter = 0
        for question in questions:  # type: ignore
            try:
                choice = question.get("choice")
                question_object = subject.get(id=question.get("question_id"))
                print(question_object.pk)
                try:
                    print("Question Object PK: ", question_object.pk)
                    print("Choice: ", choice)
                    variations = Variation.objects.filter(question_id=question_object.pk).get(id=choice)
                    print("Variation: ", variations)
                # except:
                #     print("Variation: ", variations)
                except ObjectDoesNotExist:
                    return Response(
                        data={
                            "msg": f"Variation with id: {question_object.pk} does not exist"
                        },
                        status=HTTP_404_NOT_FOUND
                    )
                if variations.is_correct:  # type: ignore
                    score += 1
            # except:
            #     print("Subject", subject)
            except ObjectDoesNotExist:
                return Response(
                    data={
                        "msg": f"Subject with id: {subject_id} does not exist!"
                    },
                    status=HTTP_404_NOT_FOUND
                )

        print("Score: ", score)  # type: ignore
        return Response(
            data={
                "score": score, 
                "user": request.user.id, 
                "subject_id": subject_id
            }, 
            status=HTTP_201_CREATED
        )
