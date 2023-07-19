from rest_framework import generics
from apps.application.api_endpoints.Create.serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from apps.application.models import Application
from rest_framework.parsers import MultiPartParser, FormParser


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


__all__ = ['ApplicationCreateView']
