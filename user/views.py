from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.serializers import UserManageSerializer, UserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ManageUserView(RetrieveUpdateAPIView):
    serializer_class = UserManageSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
