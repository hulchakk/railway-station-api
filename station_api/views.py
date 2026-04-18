from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from station_api.serializers import (
    CrewSerializer,
    JourneyListSerializer,
    JourneySerializer,
    RouteListSerializer,
    RouteRetrieveSerializer,
    RouteSerializer,
    JourneyRetrieveSerializer,
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
    Ticket,
    Train,
    TrainType,
)


class CrewViewSet(ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

    def get_queryset(self):
        queryset = self.queryset

        first_name_startswith = self.request.query_params.get(
            "first_name_startswith"
        )
        last_name_startswith = self.request.query_params.get(
            "last_name_startswith"
        )

        if first_name_startswith:
            queryset = queryset.filter(
                first_name__istartswith=first_name_startswith
            )
        if last_name_startswith:
            queryset = queryset.filter(
                last_name__istartswith=last_name_startswith
            )

        return queryset


class JourneyViewSet(ModelViewSet):
    queryset = Journey.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        departure_at = self.request.query_params.get("departure_at")
        arrival_at = self.request.query_params.get("arrival_at")

        if source:
            queryset = queryset.filter(
                route__source=source
            )
        if destination:
            queryset = queryset.filter(
                route__destination=destination
            )
        if departure_at:
            queryset = queryset.filter(
                departure_time=departure_at
            )
        if arrival_at:
            queryset = queryset.filter(
                arrival_time=arrival_at
            )

        return queryset.select_related(
            "route__source",
            "route__destination",
            "train__train_type"
        ).prefetch_related(
            "crew",
        )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return JourneyRetrieveSerializer
        if self.action == "list":
            return JourneyListSerializer

        return JourneySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_queryset(self):
        tickets_prefetch = Prefetch(
            "tickets",
            queryset=Ticket.objects.select_related(
                "journey__route__source",
                "journey__route__destination",
                "journey__train__train_type"
            )
        )
        queryset = self.queryset

        date_before = self.request.query_params.get("date_before")
        date_after = self.request.query_params.get("date_after")

        if date_before:
            queryset = queryset.filter(
                created_at__lte=date_before
            )
        if date_after:
            queryset = queryset.filter(
                created_at__gte=date_after
            )

        return queryset.filter(
            user=self.request.user
        ).select_related("user").prefetch_related(tickets_prefetch)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer

        return OrderSerializer


class RouteViewSet(ModelViewSet):
    queryset = Route.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")

        if source:
            queryset = queryset.filter(
                source=source
            )
        if destination:
            queryset = queryset.filter(
                destination=destination
            )

        return queryset.select_related(
            "source",
            "destination"
        )

    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer
        if self.action == "retrieve":
            return RouteRetrieveSerializer

        return RouteSerializer


class StationViewSet(ModelViewSet):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        name_startswith = self.request.query_params.get("name_startswith")

        if name_startswith:
            queryset = queryset.filter(
                name__istartswith=name_startswith
            )

        return queryset


class TrainViewSet(ModelViewSet):
    queryset = Train.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        name_startswith = self.request.query_params.get("name_startswith")
        train_type = self.request.query_params.get("train_type")

        if name_startswith:
            queryset = queryset.filter(
                name__istartswith=name_startswith
            )
        if train_type:
            queryset = queryset.filter(
                train_type=train_type
            )

        return queryset.select_related(
            "train_type",
        )

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TrainListSerializer

        return TrainSerializer


class TrainTypeViewSet(ModelViewSet):
    serializer_class = TrainTypeSerializer
    queryset = TrainType.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        name_startswith = self.request.query_params.get("name_startswith")

        if name_startswith:
            queryset = queryset.filter(
                name__istartswith=name_startswith
            )

        return queryset
