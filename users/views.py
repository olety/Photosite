from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User

def profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    template = loader.get_template('users/user.html')
    context = {
        'username' : user_profile.username
    }
    return HttpResponse(template.render(context=context, request=request))


def register(request):
    return HttpResponse("REGISTER")


def login(request):
    return HttpResponse("LOGIN")
