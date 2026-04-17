from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    JourneySerializer,
    RouteListSerializer,
    RouteSerializer,
    StationSerializer,
    TicketSerializer,
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
    Ticket,
    Order,
    Train,
    TrainType,
)


class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects
    serializer_class = JourneySerializer


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects


class OrderViewSet(ModelViewSet):
    queryset = Order.objects

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
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
