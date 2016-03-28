from django.conf.urls import url
from . import views

urlpatterns = [
    # /users/512
    url(r'^(?P<user_id>[0-9]+)$', views.profile, name='users_profile'),
]