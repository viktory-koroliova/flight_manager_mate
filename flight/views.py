from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from flight.forms import CrewMemberCreationForm, CrewMemberUpdateForm, FlightForm, FlightSearchForm, \
    CrewMemberSearchForm, RouteSearchForm
from flight.models import (
    Aircraft,
    CrewMember,
    Route,
    Position,
    DesignBureau,
    Flight,
)


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CrewMemberListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = CrewMemberSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = CrewMember.objects.prefetch_related("flights")
        form = CrewMemberSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(last_name__icontains=form.cleaned_data["last_name"])
        return queryset


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
    template_name = "flight/crew_form.html"
    success_url = reverse_lazy("flight:crew-list")
    form_class = CrewMemberUpdateForm


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RouteListView, self).get_context_data(**kwargs)
        departure_airport = self.request.GET.get("departure_airport", "")
        context["search_form"] = RouteSearchForm(
            initial={"departure_airport": departure_airport}
        )
        return context

    def get_queryset(self):
        queryset = Route.objects.all()
        form = RouteSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(departure_airport__icontains=form.cleaned_data["departure_airport"])
        return queryset


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FlightListView, self).get_context_data(**kwargs)
        number = self.request.GET.get("number", "")
        context["search_form"] = FlightSearchForm(
            initial={"number": number}
        )
        return context

    def get_queryset(self):
        queryset = Flight.objects.select_related("aircraft")
        form = FlightSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(number__icontains=form.cleaned_data["number"])
        return queryset


class FlightDetailView(LoginRequiredMixin, generic.DetailView):
    model = Flight


class FlightCreateView(LoginRequiredMixin, generic.CreateView):
    model = Flight
    success_url = reverse_lazy("flight:flight-list")
    form_class = FlightForm


class FlightUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Flight
    success_url = reverse_lazy("flight:flight-list")
    form_class = FlightForm


class FlightDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Flight
    success_url = reverse_lazy("flight:flight-list")


def archive(request):
    return render(request, "flight/archive.html")


def contact(request):
    return render(request, "flight/contact.html")


@login_required
def article(request):
    return render(request, "flight/article.html")
