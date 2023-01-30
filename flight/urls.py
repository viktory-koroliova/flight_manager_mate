from django.urls import path

from flight import views


urlpatterns = [
    path("", views.index, name="index"),
    path("positions/", views.PositionListView.as_view(), name="position-list"),
    path(
        "positions/<int:pk>/",
        views.PositionDetailView.as_view(),
        name="position-detail"),
    path(
        "positions/create/",
        views.PositionCreateView.as_view(),
        name="position-create"),
    path(
        "positions/<int:pk>/update/",
        views.PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        views.PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path(
        "bureaus/",
        views.DesignBureauListView.as_view(),
        name="design-bureau-list"),
    path(
        "bureaus/create/",
        views.DesignBureauCreateView.as_view(),
        name="design-bureau-create"
    ),
    path(
        "bureaus/<int:pk>/update/",
        views.DesignBureauUpdateView.as_view(),
        name="design-bureau-update",
    ),
    path(
        "bureaus/<int:pk>/delete/",
        views.DesignBureauDeleteView.as_view(),
        name="design-bureau-delete",
    ),
    path("crew/", views.CrewMemberListView.as_view(), name="crew-list"),
    path(
        "crew/<int:pk>/",
        views.CrewMemberDetailView.as_view(),
        name="crew-detail"),
    path("crew/create/", views.CrewMemberCreateView.as_view(), name="crew-create"),
    path(
        "crew/<int:pk>/update/",
        views.CrewMemberUpdateView.as_view(),
        name="crew-update"),
    path(
        "crew/<int:pk>/delete/",
        views.CrewMemberDeleteView.as_view(),
        name="crew-delete"),
    path("aircraft/", views.AircraftListView.as_view(), name="aircraft-list"),
    path(
        "aircraft/<int:pk>/",
        views.AircraftDetailView.as_view(),
        name="aircraft-detail"),
    path(
        "aircraft/create/",
        views.AircraftCreateView.as_view(),
        name="aircraft-create"),
    path(
        "aircraft/<int:pk>/update/",
        views.AircraftUpdateView.as_view(),
        name="aircraft-update",
    ),
    path(
        "aircraft/<int:pk>/delete/",
        views.AircraftDeleteView.as_view(),
        name="aircraft-delete",
    ),
    path("routes/", views.RouteListView.as_view(), name="route-list"),
    path("routes/<int:pk>/", views.RouteDetailView.as_view(), name="route-detail"),
    path("routes/create/", views.RouteCreateView.as_view(), name="route-create"),
    path(
        "routes/<int:pk>/update/",
        views.RouteUpdateView.as_view(),
        name="route-update"),
    path(
        "routes/<int:pk>/delete/",
        views.RouteDeleteView.as_view(),
        name="route-delete"),
    path("flights/", views.FlightListView.as_view(), name="flight-list"),
    path(
        "flights/<int:pk>/",
        views.FlightDetailView.as_view(),
        name="flight-detail"),
    path("flights/create/", views.FlightCreateView.as_view(), name="flight-create"),
    path(
        "flights/<int:pk>/update/",
        views.FlightUpdateView.as_view(),
        name="flight-update"),
    path(
        "flights/<int:pk>/delete/",
        views.FlightDeleteView.as_view(),
        name="flight-delete"),
    path("archive/", views.archive, name="archive"),
    path("contact/", views.contact, name="contact"),
    path("article/", views.article, name="article"),
]

app_name = "flight"
