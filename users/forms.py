from django.contrib.auth import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate
from .models import User
# import sys


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = forms.UserCreationForm.Meta.fields + ('cameras', 'lenses')


class LoginForm(forms.AuthenticationForm):
    pass
