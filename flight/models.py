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
