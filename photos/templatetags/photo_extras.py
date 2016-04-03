from django import template


register = template.Library()


@register.filter
def has_liked(photo, user):
    return photo.like_set.filter(user=user).count() > 0
