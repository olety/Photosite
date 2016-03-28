import user

from django.shortcuts import render
# from django.template import loader
from django.http import Http404, HttpResponseRedirect
from .models import User
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import forms
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
# from photos.views import home
from .forms import LoginForm


# @login_required(login_url='/login/')
def profile(request, user_id):
    try:
        user_profile = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("Requested user doesn't exist.")
    context = {
        'username': user_profile.username
    }
    return render(request, 'users/user.html', context=context)


def register(request):
    return render(request, 'users/register.html')


def base(request):
    return render(request, 'base.html', context={'user':request.user})


def password_reset(request):
    return render(request, 'base.html', context={'user':request.user})


def login(request):
    # Maybe there's a better way to do this? Not logging stuff out every time I mean
    # TODO(Olexiy): Figure out how to redirect to the next page
    auth_logout(request)
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
                auth_login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm(request)

    return render(request, 'users/login.html', context={
        'form': form,
    })


def logout(request):
    auth_logout(request)
    next_page = ''
    if request.GET:
        next_page = request.GET['next']
    if next_page != '':
        return HttpResponseRedirect(next_page)
    else:
        return HttpResponseRedirect('/')

