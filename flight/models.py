from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)


class DesignBureau(models.Model):
    name = models.CharField(max_length=255)
    headquarter = models.CharField(max_length=255)

