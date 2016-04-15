from django import template


register = template.Library()


@register.filter
def has_liked(user, photo):
    return user.is_authenticated() and photo.like_set.filter(user=user).count() > 0
