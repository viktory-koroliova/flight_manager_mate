from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from flight.models import (
    Aircraft,
    CrewMember,
    Route,
    Position,
    DesignBureau,
    Flight,
)


@login_required
def index(request):
    context = {
        "aircraft": Aircraft.objects.all().values("type"),
        "crew": CrewMember.objects.all().values("username"),
        "routes": Route.objects.all().values("departure_airport"),

    }
    return render(request, "flight/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position


class PositionDetailView(generic.DetailView):
    model = Position
    queryset = Position.objects.prefetch_related("crew")


class DesignBureauListView(generic.ListView):
    model = DesignBureau
    context_object_name = "design_bureau_list"


class FlightListView(generic.ListView):
    model = Flight
    paginate_by = 5
