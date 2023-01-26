from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)


class DesignBureau(models.Model):
    name = models.CharField(max_length=255)
    headquarter = models.CharField(max_length=255)


class CrewMember(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=63)
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE, null=True, related_name="crew")


class Aircraft(models.Model):
    AIRCRAFT_WTC_CHOICES = (
        ("L", "Light"),
        ("M", "Medium"),
        ("H", "Heavy")
    )
    type = models.CharField(max_length=63)
    age = models.IntegerField()
    wake_turbulence_category = models.CharField(
        max_length=1,
        choices=AIRCRAFT_WTC_CHOICES
    )
    design_bureau = models.ForeignKey(to=DesignBureau, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "aircraft"


class Route(models.Model):
    departure_airport = models.CharField(max_length=255)
    arrival_airport = models.CharField(max_length=255)
    duration = models.DurationField()


class Flight(models.Model):
    number = models.CharField(max_length=255)
    departure = models.DateTimeField()
    route = models.ForeignKey(to=Route, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(to=Aircraft, on_delete=models.CASCADE)
    crew = models.ManyToManyField(to=CrewMember, related_name="flights")
    is_delayed = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=["number", "departure"],
            name="unique_flight"
        )]