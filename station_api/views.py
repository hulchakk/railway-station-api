from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
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
    Journey,
    Route,
    Station,
    Order,
    Train,
    TrainType,
)


class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects
    serializer_class = JourneySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return RouteListSerializer

        return RouteSerializer


class StationViewSet(ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects


class TrainViewSet(ModelViewSet):
    queryset = Train.objects

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TrainListSerializer

        return TrainSerializer


class TrainTypeViewSet(ModelViewSet):
    serializer_class = TrainTypeSerializer
    queryset = TrainType.objects
