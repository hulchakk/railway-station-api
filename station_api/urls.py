from django.urls import path, include
from rest_framework.routers import DefaultRouter

from station_api.views import (
    JourneyViewSet,
    RouteViewSet,
    StationViewSet,
    TicketViewSet,
    OrderViewSet,
    TrainTypeViewSet,
    TrainViewSet,
)


router = DefaultRouter()

router.register("journeys", JourneyViewSet)
router.register("tickets", TicketViewSet)
router.register("orders", OrderViewSet)
router.register("routs", RouteViewSet)
router.register("stations", StationViewSet)
router.register("trains", TrainViewSet)
router.register("train_types", TrainTypeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]


app_name = "station_api"
