from django.urls import path, include
from rest_framework.routers import DefaultRouter

from station_api.views import (
    JourneyViewSet,
    TicketViewSet,
    OrderViewSet,
)


router = DefaultRouter()

router.register("journeys", JourneyViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)


urlpatterns = [
    path("", include(router.urls)),
]


app_name = "station_api"
