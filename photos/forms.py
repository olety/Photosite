from django import forms
from django.forms import ValidationError
from .models import Photo
# import sys


class UploadForm(forms.ModelForm):

    title = forms.CharField(label='Title', required=False)
    description = forms.CharField(label='Description', required=False)
    image = forms.ImageField(label='Image', required=True)

    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']
