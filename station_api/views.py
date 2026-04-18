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
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()

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
