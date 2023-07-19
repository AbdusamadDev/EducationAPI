from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.api_endpoints import CreateUserView, LoginByEmailnView


application_urlpatterns = [
    path("", CreateUserView.as_view(), name="user-register"),
    path("login/", LoginByEmailnView.as_view(), name="user-login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
urlpatterns = application_urlpatterns
