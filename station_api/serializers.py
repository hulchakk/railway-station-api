from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from station_api.models import (
    Journey,
    Ticket,
)


class JourneySerializer(ModelSerializer):
    class Meta:
        model = Journey
        fields = (
            "id",
            "route",
            "train",
            "departure_time",
            "arrival_time",
        )


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "cargo",
            "seat",
            "journey",
            "order",
        )
