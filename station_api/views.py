from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    JourneySerializer,
)
from station_api.models import (
    Journey
)


class JourneyViewSet(ModelViewSet):
    serializer_class = JourneySerializer
    queryset = Journey.objects
