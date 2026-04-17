from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    JourneySerializer,
    TicketSerializer,
)
from station_api.models import (
    Journey,
    Ticket,
)


class JourneyViewSet(ModelViewSet):
    serializer_class = JourneySerializer
    queryset = Journey.objects


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects
