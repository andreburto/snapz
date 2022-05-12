from django.contrib import admin

from . import models


class FullnameMixin:
    def person_fullname(self, instance):
        return f"{instance.person.last_name}, {instance.person.first_name}"


# Register your models here.
@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', )
    ordering = ('title', 'filename', )
    readonly_fields = ('filename', 'base64_filename', )


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('filename', )


@admin.register(models.Thumb)
class ThumbAdmin(admin.ModelAdmin):
    list_display = ('filename', 'show_thumbnail', )
    readonly_fields = ('filename', )


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VideoPeople)
class VideoPeopleAdmin(admin.ModelAdmin, FullnameMixin):
    list_display = ('video_title', 'person_fullname', 'role', 'video_url', )

    def video_title(self, instance):
        return instance.video



@admin.register(models.LinkPeople)
class LinkPeopleAdmin(admin.ModelAdmin, FullnameMixin):
    list_display = ('edit_text', 'show_link', 'person_fullname', )

    def edit_text(self, instance):
        return "Edit"

    def show_link(self, instance):
        return instance.link.show_link()
