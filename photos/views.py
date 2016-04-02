from django.shortcuts import render


# Create your views here.
# TODO: Tsvetan
def home(request, context={}):
    new_context = context.copy()
    new_context.update({
                'user': request.user,
                })
    return render(request, 'base.html', context=context)


def upload(request, context={}):

    return render(request, 'base.html', context=context)
