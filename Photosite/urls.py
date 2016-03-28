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
from django.contrib.auth import views as django_views
from photos import views as photo_views
from users import views as user_views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    # PHOTOS
    #  /
    url(r'^$', photo_views.home, name='photos_home'),
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
