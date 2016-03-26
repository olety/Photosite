from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    html = "Name : " + str(user_profile)

    return HttpResponse(html)


def register(request):
    return HttpResponse("REGISTER")


def login(request):
    return HttpResponse("LOGIN")


def feed(request):
    return HttpResponse("HOME PAGE")