from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<photo_id>[0-9]+)$', views.view, name='photos_view'),
    url(r'^upload$', views.upload, name='photos_upload')
]