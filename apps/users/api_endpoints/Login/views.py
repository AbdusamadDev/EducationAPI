from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.Login.serializers import LoginByEmailSerializer


class LoginByEmailnView(APIView):

    def post(self, request):
        serializer = LoginByEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


__all__ = ["LoginByEmailnView"]
