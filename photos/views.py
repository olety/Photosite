from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Photo
from .models import Tag
from .models import Comment


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
            photo = form.save(commit=False)
            # photo = Photo(
            #     title=form.cleaned_data['title'],
            #     description=form.cleaned_data['description'],
            #     image=form.cleaned_data['image'],
            #     author=request.user
            # )
            photo.author = request.user
            photo.save()

            # photo.tags

            for t in form.cleaned_data['tags'].split(','):
                t = t.strip()
                tag, created = Tag.objects.get_or_create(name=t)

                if created:
                    tag.save()

                photo.tags.add(tag)

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


def comment_add(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
    except ObjectDoesNotExist:
        raise Http404('Photo does not exist')

    if not request.user.is_authenticated():
        raise PermissionDenied('User not logged in')

    content = request.POST.get('content', '').strip()
    url_append = '#comments'

    if len(content) > 2:
        comment = Comment(
            photo=photo,
            user=request.user,
            content=content
        )
        comment.save()
        url_append = '#comment_' + str(comment.id)
    else:
        messages.error(request, 'Comment is too short.')

    return HttpResponseRedirect(reverse('photos_view', args=[photo.id]) + url_append)
