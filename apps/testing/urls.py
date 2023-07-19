from django.urls import path

from apps.testing import (
    Create,
    List,
    Delete,
    Details,
    Update
)

list_urls = [
    path("list/", List.views.TestResultListAPIView.as_view()),
    path("subjects/list/", List.views.SubjectListAPIView.as_view()),
    path("variations/<int:pk>/list/", List.views.VariationListAPIView.as_view()),
    path("questions/list/", List.views.QuestionListAPIView.as_view()),
]

create_urls = [
    path("variations/create/", Create.views.VariationCreateAPIView.as_view()),
    path("create/", Create.views.TestResultCreateAPIView.as_view()),  # Students
    path("subjects/create/", Create.views.SubjectCreateAPIView.as_view()),
    path("questions/create/", Create.views.QuestionsCreateAPIView.as_view())
]

update_urls = [
    path("questions/<int:pk>/edit/", Update.views.QuestionEditAPIView.as_view()),
    path("variations/<int:pk>/edit/", Update.views.VariationEditAPIView.as_view()),
]

details_urls = [
    path("<int:pk>/details/", Details.views.TestResultRetrieveAPIView.as_view()),
    path("questions/<int:pk>/details/", Details.views.QuestionRetrieveAPIView.as_view()),
    path("subjects/<int:pk>/details/", Details.views.SubjectRetrieveAPIView.as_view()),
    path("variations/<int:pk>/details/", Details.views.VariationRetrieveAPIView.as_view()),
]

delete_urls = [
    path("questions/<int:pk>/delete/", Delete.views.QuestionDeleteAPIView.as_view()),
    path("variations/<int:pk>/delete/", Delete.views.VariationDeleteAPIView.as_view()),
    path("subjects/<int:pk>/delete/", Delete.views.SubjectDeleteAPIView.as_view()),
    path("<int:pk>/delete/", Delete.views.TestResultDeleteAPIView.as_view())
]

urlpatterns = list_urls + create_urls + details_urls + update_urls + delete_urls
