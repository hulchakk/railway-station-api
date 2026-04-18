from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import (
    ObtainAuthToken as DrfObtainAuthToken
)
from rest_framework.settings import api_settings
from rest_framework.permissions import AllowAny

from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ObtainAuthToken(DrfObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
