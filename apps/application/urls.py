from django.urls import path
from apps.application.api_endpoints import ApplicationCreateView, ApplicationListView

urlpatterns = [
    path('', ApplicationCreateView.as_view(), name='application-create'),
    path('list/', ApplicationListView.as_view(), name='application-list'),
]
