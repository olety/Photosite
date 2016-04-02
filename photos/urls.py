from django.conf.urls import url
from . import views

urlpatterns = [
    # /users/512
    url(r'^upload$', views.upload, name='photos_upload'),
]