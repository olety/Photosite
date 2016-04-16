from __future__ import unicode_literals
from django.db import models
from users.models import User
from datetime import datetime
import os
import binascii


def photo_upload_path(instance, filename):
    date = datetime.now()
    return 'photos/{1}/{2}/{0}.{3}'.format(
        binascii.hexlify(os.urandom(16)),
        date.strftime('%Y'),
        date.strftime('%m'),
        os.path.splitext(filename)[1][1:].strip().lower()
    )


class Tag (models.Model):

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )


class Photo (models.Model):

    id = models.AutoField(
        primary_key=True
    )

    image = models.ImageField(
        upload_to=photo_upload_path
    )

    title = models.CharField(
        max_length=100,
        default='Untitled',
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

    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def has_liked(self, user):
        return self.like_set.filter(user=user).count() > 0

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = "photos"


class Like (models.Model):

    id = models.AutoField(
        primary_key=True
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (('photo', 'user'),)


class Comment (models.Model):

    id = models.AutoField(
        primary_key=True
    )

    content = models.TextField()

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
