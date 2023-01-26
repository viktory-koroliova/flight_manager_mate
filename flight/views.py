from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from flight.forms import CrewMemberCreationForm
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


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("flight:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("flight:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("flight:position-list")


class DesignBureauListView(LoginRequiredMixin, generic.ListView):
    model = DesignBureau
    template_name = "flight/design_bureau_list.html"
    paginate_by = 5


class DesignBureauCreateView(LoginRequiredMixin, generic.CreateView):
    model = DesignBureau
    fields = "__all__"
    template_name = "flight/design_bureau_form.html"
    success_url = reverse_lazy("flight:design-bureau-list")


class DesignBureauUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DesignBureau
    fields = "__all__"
    template_name = "flight/design_bureau_form.html"
    success_url = reverse_lazy("flight:design-bureau-list")


class DesignBureauDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DesignBureau
    template_name = "flight/design_bureau_confirm_delete.html"
    success_url = reverse_lazy("flight:design-bureau-list")


class CrewMemberListView(LoginRequiredMixin, generic.ListView):
    model = CrewMember
    template_name = "flight/crew_list.html"
    paginate_by = 5


class CrewMemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = CrewMember
    template_name = "flight/crew_detail.html"
    queryset = CrewMember.objects.prefetch_related("flights__route")


class CrewMemberCreateView(LoginRequiredMixin, generic.CreateView):
    model = CrewMember
    template_name = "flight/crew_form.html"
    success_url = reverse_lazy("flight:crew-list")
    form_class = CrewMemberCreationForm


class CrewMemberUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CrewMember
    fields = "__all__"
    template_name = "flight/crew_form.html"
    success_url = reverse_lazy("flight:crew-list")


class CrewMemberDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CrewMember
    template_name = "flight/crew_confirm_delete.html"
    success_url = reverse_lazy("flight:crew-list")


class AircraftListView(LoginRequiredMixin, generic.ListView):
    model = Aircraft
    paginate_by = 5


class AircraftDetailView(LoginRequiredMixin, generic.DetailView):
    model = Aircraft


class AircraftCreateView(LoginRequiredMixin, generic.CreateView):
    model = Aircraft
    fields = "__all__"
    success_url = reverse_lazy("flight:aircraft-list")


class AircraftUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Aircraft
    fields = "__all__"
    success_url = reverse_lazy("flight:aircraft-list")


class AircraftDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Aircraft
    success_url = reverse_lazy("flight:aircraft-list")


class RouteListView(LoginRequiredMixin, generic.ListView):
    model = Route
    paginate_by = 5


class RouteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Route


class RouteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Route
    fields = "__all__"
    success_url = reverse_lazy("flight:route-list")


class RouteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Route
    fields = "__all__"
    success_url = reverse_lazy("flight:route-list")


class RouteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Route
    success_url = reverse_lazy("flight:route-list")


class FlightListView(LoginRequiredMixin, generic.ListView):
    model = Flight
    paginate_by = 5


class FlightDetailView(LoginRequiredMixin, generic.DetailView):
    model = Flight


class FlightCreateView(LoginRequiredMixin, generic.CreateView):
    model = Flight
    fields = "__all__"
    success_url = reverse_lazy("flight:flight-list")


class FlightUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Flight
    fields = "__all__"
    success_url = reverse_lazy("flight:flight-list")


class FlightDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Flight
    success_url = reverse_lazy("flight:flight-list")
