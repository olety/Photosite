from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<photo_id>[0-9]+)$', views.view, name='photos_view'),
    url(r'^(?P<photo_id>[0-9]+)/like$', views.like, name='photos_like_toggle'),
    url(r'^upload$', views.upload, name='photos_upload')
]