from django.urls import path

from flight.views import (
    index,
    PositionListView,
    PositionDetailView,
    DesignBureauListView,
    FlightListView
)


urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("bureaus/", DesignBureauListView.as_view(), name="design-bureau-list"),
    path("flights/", FlightListView.as_view(), name="flight-list")
    ]

app_name = "flight"
