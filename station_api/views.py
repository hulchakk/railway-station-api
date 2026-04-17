from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    JourneySerializer,
    TicketSerializer,
    OrderSerializer,
    OrderListSerializer,
)
from station_api.models import (
    Journey,
    Ticket,
    Order,
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
