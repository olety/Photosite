from django import forms
from django.forms import ValidationError
from .models import Photo
from users.models import Camera
from users.models import Lens
# import sys


class UploadForm(forms.ModelForm):

    title = forms.CharField(label='Title', required=False)
    description = forms.CharField(label='Description', required=False)
    image = forms.ImageField(label='Image', required=True)
    tags = forms.CharField(label='Tags', required=True)
    camera = forms.ModelChoiceField(queryset=Camera.objects.all(), label='Camera', required=False)
    lens = forms.ModelChoiceField(queryset=Lens.objects.all(), label='Lens', required=False)

    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'camera', 'lens']
