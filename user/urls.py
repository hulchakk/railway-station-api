from django.urls import path

from user.views import (
    CreateUserView,
    ObtainAuthToken
)


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", ObtainAuthToken.as_view(), name="token_obtain"),
]


app_name = "user"
