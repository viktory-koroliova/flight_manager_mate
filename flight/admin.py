from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from flight.models import CrewMember, Position, DesignBureau, Aircraft, Route, Flight


@admin.register(CrewMember)
class AdminCrewMember(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", "position")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("license_number", "position")}),)
    )
    list_filter = ("position",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license_number",
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(DesignBureau)
class AdminDesignBureau(admin.ModelAdmin):
    list_display = ("name", "headquarter", )


@admin.register(Aircraft)
class AdminAircraft(admin.ModelAdmin):
    list_display = ("type", "design_bureau", "age", "wake_turbulence_category")
    list_filter = ("design_bureau", "wake_turbulence_category")


@admin.register(Route)
class AdminRoute(admin.ModelAdmin):
    list_display = ("departure_airport", "arrival_airport", "duration")
    list_filter = ("departure_airport", "arrival_airport")


@admin.register(Flight)
class AdminFlight(admin.ModelAdmin):
    list_display = ("number", "route", "departure", "aircraft", "is_delayed")
    list_filter = ("route", "number", "is_delayed")


admin.site.register(Position)
