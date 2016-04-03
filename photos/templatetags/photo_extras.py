from django import template


register = template.Library()


@register.filter
def has_liked(user, photo):
    return photo.like_set.filter(user=user).count() > 0
