from django.conf.urls import url
from . import views

urlpatterns = [
    # /users/512
    url(r'^user/(?P<user_id>[0-9]+)$', views.profile, name=''),

    # /register/
    url(r'^register/', views.register, name=''),

    # /login/
    url(r'^login/', views.login, name=''),

    # / (homepage)
    url(r'^$', views.feed, name=''),
]