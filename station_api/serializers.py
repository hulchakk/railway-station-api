from django.db import transaction
from rest_framework import serializers
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


class RouteRetrieveSerializer(RouteSerializer):
    source = StationSerializer()
    destination = StationSerializer()


class RouteListSerializer(RouteSerializer):
    source = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    destination = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )


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
    train_type = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
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


class JourneyRetrieveSerializer(JourneySerializer):
    crew = CrewSerializer(many=True)
    route = RouteListSerializer()
    train = TrainListSerializer()


class JourneyListSerializer(ModelSerializer):
    rout_source = serializers.CharField(
        source="route.source.name",
        read_only=True
    )
    rout_destination = serializers.CharField(
        source="route.destination.name",
        read_only=True
    )
    train = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Journey
        fields = (
            "id",
            "rout_source",
            "rout_destination",
            "train",
            "departure_time",
            "arrival_time",
        )
