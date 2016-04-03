"""Photosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as django_static_serve
from photos import views as photo_views
from users import views as user_views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^uploads/(?P<path>.*)$', django_static_serve, {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True
    }),
    url(r'^static/(?P<path>.*)$', django_static_serve, {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True
    }),

    #  /
    url(r'^$', photo_views.home, name='global_home'),

    # PHOTOS
    # /photo/
    url(r'^photo/', include('photos.urls')),

    # USERS
    # /user/
    url(r'^user/', include('users.urls')),

    # /login
    url(r'^login', user_views.login, name='users_login'),
    # /logout
    url(r'^logout', user_views.logout, name='users_logout'),
    # /register
    url(r'^register', user_views.register, name='users_register'),
    # /reset
    url(r'^reset/$', user_views.password_reset, name='users_password_reset'),
    # /admin/
    url(r'^admin/', include(admin.site.urls)),

]
