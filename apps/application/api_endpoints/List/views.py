from rest_framework import generics
from apps.application.api_endpoints.List.serializers import ApplicationListSerializer
from rest_framework.permissions import IsAdminUser
from apps.application.models import Application


class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAdminUser]


__all__ = ['ApplicationListView']
