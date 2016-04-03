from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UploadForm
from .models import Photo


def home(request):
    # new_context = context.copy()
    # new_context.update({
    #             'user': request.user,
    #             })

    photos = Photo.objects.order_by('created_at')[:10]

    return render(request, 'photos/feed.html', context={
        'photos': photos
    })


def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            photo = Photo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
                author=request.user
            )
            photo.save()

            return HttpResponseRedirect(reverse('photos_view', args=[photo.id]))
    else:
        form = UploadForm()

    return render(request, 'photos/upload.html', context={
        'form': form
    })


def view(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return render(request, 'photos/view.html', context={
        'photo': photo
    })

