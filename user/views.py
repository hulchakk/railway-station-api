from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import (
    ObtainAuthToken as DrfObtainAuthToken
)
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class ObtainAuthToken(DrfObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
