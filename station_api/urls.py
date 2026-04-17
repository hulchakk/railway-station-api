from django.urls import path, include
from rest_framework.routers import DefaultRouter

from station_api.views import (
    JourneyViewSet,
)


router = DefaultRouter()

router.register("journeys", JourneyViewSet)


urlpatterns = [
    path("", include(router.urls)),
]


app_name = "station_api"
