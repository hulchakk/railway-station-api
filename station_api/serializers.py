from django.db import transaction
from rest_framework.serializers import ModelSerializer

from station_api.models import (
    Crew,
    Journey,
    Ticket,
    Order,
    Route,
    Station,
    Train,
    TrainType,
)


class CrewSerializer(ModelSerializer):
    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class JourneySerializer(ModelSerializer):
    class Meta:
        model = Journey
        fields = (
            "id",
            "route",
            "train",
            "crew",
            "departure_time",
            "arrival_time",
        )


class JourneyListSerializer(JourneySerializer):
    crew = CrewSerializer(many=True)


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


class OrderSerializer(ModelSerializer):
    tickets = TicketSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "tickets",
        )

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Order.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "tickets",
        )


class StationSerializer(ModelSerializer):
    class Meta:
        model = Station
        fields = (
            "id",
            "name",
            "latitude",
            "longitude",
        )


class RouteSerializer(ModelSerializer):
    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "destination",
            "distance",
        )


class RouteListSerializer(RouteSerializer):
    source = StationSerializer()
    destination = StationSerializer()


class TrainTypeSerializer(ModelSerializer):
    class Meta:
        model = TrainType
        fields = (
            "id",
            "name",
        )


class TrainSerializer(ModelSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "cargo_num",
            "places_in_cargo",
            "train_type",
        )


class TrainListSerializer(TrainSerializer):
    train_type = TrainTypeSerializer()
