from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    CrewSerializer,
    JourneyListSerializer,
    JourneySerializer,
    RouteListSerializer,
    RouteSerializer,
    StationSerializer,
    OrderSerializer,
    OrderListSerializer,
    TrainListSerializer,
    TrainSerializer,
    TrainTypeSerializer,
)
from station_api.models import (
    Crew,
    Journey,
    Route,
    Station,
    Order,
    Ticket,
    Train,
    TrainType,
)


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects.all()

    def get_queryset(self):
        return self.queryset.select_related(
            "route__source",
            "route__destination",
            "train__train_type"
        ).prefetch_related(
            "crew",
        )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return JourneyListSerializer

        return JourneySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_queryset(self):
        tickets_prefetch = Prefetch(
            "tickets",
            queryset=Ticket.objects.select_related(
                "journey__route__source",
                "journey__route__destination",
                "journey__train__train_type"
            )
        )

        return self.queryset.filter(
            user=self.request.user
        ).select_related("user").prefetch_related(tickets_prefetch)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()

    def get_queryset(self):
        return self.queryset.select_related(
            "source",
            "destination"
        )

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return RouteListSerializer

        return RouteSerializer


class StationViewSet(ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class TrainViewSet(ModelViewSet):
    queryset = Train.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TrainListSerializer

        return TrainSerializer


class TrainTypeViewSet(ModelViewSet):
    serializer_class = TrainTypeSerializer
    queryset = TrainType.objects.all()
