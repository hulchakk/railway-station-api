from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from station_api.models import (
    Journey,
    Ticket,
    Order,
    Route,
    Station,
    Train,
    TrainType,
)
from user.serializers import UserSerializer


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


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
        )


class OrderListSerializer(OrderSerializer):
    user = UserSerializer()


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
