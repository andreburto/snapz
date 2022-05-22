from django.contrib import admin
from django.utils.html import format_html

from . import models


class FullnameMixin(admin.ModelAdmin):
    def person_fullname(self, instance):
        return f"{instance.person.last_name}, {instance.person.first_name}"


class TagInline(admin.TabularInline):
    model = models.VideoTag
    fk_name = "video"
    extra = 0


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'studio', 'filename', 'base64_filename', ]
    inlines = [TagInline, ]
    list_display = ('title', 'video_url', )
    ordering = ('title', 'filename', )
    readonly_fields = ('filename', 'base64_filename', )


class ShowThumbnailAdmin(admin.ModelAdmin):
    fields = ['show_thumbnail', 'filename', 'video', ]
    list_display = ('filename', 'video', 'show_thumbnail', )
    ordering = ('video', 'filename', )
    readonly_fields = ('filename', 'show_thumbnail', )

    def show_thumbnail(self, instance):
        thumbnail_file = instance.filename if instance.filename.startswith("th_") else f"th_{instance.filename}"
        image_file = instance.filename.replace("th_", "")
        return format_html(
            '<a href="/static/{0}/{1}" target="_blank"><img src="/static/{0}/{2}" alt="{3}" style="border: none;"><a>',
            instance.video.base64_filename, image_file, thumbnail_file, instance.video.title)


@admin.register(models.Image)
class ImageAdmin(ShowThumbnailAdmin):
    pass


@admin.register(models.Thumb)
class ThumbAdmin(ShowThumbnailAdmin):
    pass


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VideoPeople)
class VideoPeopleAdmin(FullnameMixin):
    list_display = ('video_title', 'person_fullname', 'role', 'video_url', )

    def video_title(self, instance):
        return instance.video


@admin.register(models.LinkPeople)
class LinkPeopleAdmin(FullnameMixin):
    list_display = ('edit_text', 'show_link', 'person_fullname', )

    def edit_text(self, instance):
        return "Edit"

    def show_link(self, instance):
        return instance.link.show_link()


@admin.register(models.StudioName)
class StudioNameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StudioNameStudio)
class StudioNameStudioAdmin(admin.ModelAdmin):
    pass
