from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, Camera, Lens
from .forms import UserChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    list_display = ('id',) + UserAdmin.list_display
    list_display_links = ('id', 'username', 'email')
    fieldsets = UserAdmin.fieldsets + \
        (
            ("Gear", {
                'classes': ('extrapretty',),
                'fields': ('cameras', 'lenses')
                }),
            ("Social", {
                'classes': ('extrapretty',),
                'fields': ('view_count', 'fav_count'),
            })
        )

    filter_horizontal = UserAdmin.filter_horizontal + (
        'cameras',
        'lenses'
    )

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Lens)
class LensAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
