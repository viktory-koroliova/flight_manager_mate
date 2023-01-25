from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)

