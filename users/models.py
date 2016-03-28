from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class Camera (models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Camera'
        verbose_name_plural = "cameras"


class Lens (models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lens'
        verbose_name_plural = "lenses"


class User (AbstractUser):

    id = models.AutoField(primary_key=True)

    cameras = models.ManyToManyField(
        Camera,
        blank=True,
    )

    lenses = models.ManyToManyField(
        Lens,
        blank=True,
    )

    # Photos app will modify it
    view_count = models.DecimalField(
        verbose_name="Total number of views",
        name="view_count",
        decimal_places=10,
        max_digits=10,
        default=Decimal(0),
    )

    # Photos app will modify it
    fav_count = models.DecimalField(
        verbose_name="Total number of favorites",
        name="fav_count",
        decimal_places=0,
        max_digits=10,
        default=Decimal(0)
    )

    def __str__(self):
        return self.username

