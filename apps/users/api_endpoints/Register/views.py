from rest_framework.generics import CreateAPIView
from apps.users.api_endpoints.Register.serializers import UserCreateSerializer
from apps.users.models import User


class CreateUserView(CreateAPIView):
    """
    Create User. Authentication is not required!
    """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


__all__ = ["CreateUserView"]
