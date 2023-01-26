from django.urls import path

from flight.views import (
    index,
    PositionListView,
    PositionDetailView, PositionCreateView,
    PositionUpdateView, PositionDeleteView,
    DesignBureauListView, DesignBureauCreateView,
    DesignBureauUpdateView, DesignBureauDeleteView,
    CrewMemberListView,
    CrewMemberDetailView, CrewMemberCreateView,
    CrewMemberUpdateView, CrewMemberDeleteView,
    AircraftListView,
    AircraftDetailView, AircraftCreateView,
    AircraftUpdateView, AircraftDeleteView,
    RouteListView,
    RouteDetailView, RouteCreateView,
    RouteUpdateView, RouteDeleteView,
    FlightListView,
    FlightDetailView, FlightCreateView,
    FlightUpdateView, FlightDeleteView
)


urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

    path("bureaus/", DesignBureauListView.as_view(), name="design-bureau-list"),
    path("bureaus/create/", DesignBureauCreateView.as_view(), name="design-bureau-create"),
    path("bureaus/<int:pk>/update/", DesignBureauUpdateView.as_view(), name="design-bureau-update"),
    path("bureaus/<int:pk>/delete/", DesignBureauDeleteView.as_view(), name="design-bureau-delete"),

    path("crew/", CrewMemberListView.as_view(), name="crew-list"),
    path("crew/<int:pk>/", CrewMemberDetailView.as_view(), name="crew-detail"),
    path("crew/create/", CrewMemberCreateView.as_view(), name="crew-create"),
    path("crew/<int:pk>/update/", CrewMemberUpdateView.as_view(), name="crew-update"),
    path("crew/<int:pk>/delete/", CrewMemberDeleteView.as_view(), name="crew-delete"),

    path("aircraft/", AircraftListView.as_view(), name="aircraft-list"),
    path("aircraft/<int:pk>/", AircraftDetailView.as_view(), name="aircraft-detail"),
    path("aircraft/create/", AircraftCreateView.as_view(), name="aircraft-create"),
    path("aircraft/<int:pk>/update/", AircraftUpdateView.as_view(), name="aircraft-update"),
    path("aircraft/<int:pk>/delete/", AircraftDeleteView.as_view(), name="aircraft-delete"),

    path("routes/", RouteListView.as_view(), name="route-list"),
    path("routes/<int:pk>/", RouteDetailView.as_view(), name="route-detail"),
    path("routes/create/", RouteCreateView.as_view(), name="route-create"),
    path("routes/<int:pk>/update/", RouteUpdateView.as_view(), name="route-update"),
    path("routes/<int:pk>/delete/", RouteDeleteView.as_view(), name="route-delete"),


    path("flights/", FlightListView.as_view(), name="flight-list"),
    path("flights/<int:pk>/", FlightDetailView.as_view(), name="flight-detail"),
    path("flights/create/", FlightCreateView.as_view(), name="flight-create"),
    path("flights/<int:pk>/update/", FlightUpdateView.as_view(), name="flight-update"),
    path("flights/<int:pk>/delete/", FlightDeleteView.as_view(), name="flight-delete"),

    ]

app_name = "flight"
