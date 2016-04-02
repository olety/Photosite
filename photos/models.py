from __future__ import unicode_literals
from django.db import models
from users.models import User
import os
import binascii


def photo_upload_path(instance, filename):
    return 'photos/%Y/%m/{0}'.format(binascii.hexlify(os.urandom(16)))


class Photo (models.Model):

    id = models.AutoField(
        primary_key=True
    )

    image = models.ImageField(
        upload_to=photo_upload_path
    )

    title = models.CharField(
        max_length=100,
        default='',
        unique=False
    )

    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=False
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = "photos"
