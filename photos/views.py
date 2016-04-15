from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Photo


def home(request):
    # new_context = context.copy()
    # new_context.update({
    #             'user': request.user,
    #             })

    photos = Photo.objects.order_by('-created_at')[:10]

    return render(request, 'photos/feed.html', context={
        'photos': photos
    })


@login_required
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
    try:
        photo = Photo.objects.get(pk=photo_id)
    except ObjectDoesNotExist:
        raise Http404('Photo does not exist')

    return render(request, 'photos/view.html', context={
        'photo': photo
    })


def like(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except ObjectDoesNotExist:
        raise Http404('Photo does not exist')

    if not request.user.is_authenticated():
        raise PermissionDenied('User not logged in')

    the_like = photo.like_set.filter(user=request.user).first()

    if the_like is not None:
        the_like.delete()
    else:
        photo.like_set.create(user=request.user, photo=photo)

    return HttpResponseRedirect(reverse('photos_view', args=[photo_id]))
