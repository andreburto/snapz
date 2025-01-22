import os

from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import path
from django.utils.html import format_html

from . import models
from . import utils

from tags import models as tags_models

class FullnameMixin(admin.ModelAdmin):
    def person_fullname(self, instance):
        return f"{instance.person.last_name}, {instance.person.first_name}"


class VideoTagInline(admin.TabularInline):
    model = models.VideoTag
    fk_name = "video"
    extra = 0


class ImageTagInline(admin.TabularInline):
    model = models.ImageTag
    fk_name = "image"
    extra = 0


class ThumbTagInline(admin.TabularInline):
    model = models.ThumbTag
    fk_name = "thumb"
    extra = 0


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'studio', 'filename', 'base64_filename', ]
    inlines = [VideoTagInline, ]
    list_display = ('title', 'video_url', )
    ordering = ('title', 'filename', )
    readonly_fields = ('filename', 'base64_filename', )


class ShowThumbnailAdmin(admin.ModelAdmin):
    fields = ['show_thumbnail', 'filename', 'description', 'video', ]
    list_display = ('filename', 'video', 'show_description', 'show_thumbnail', )
    ordering = ('video', 'filename', )
    readonly_fields = ('filename', 'show_thumbnail', )

    def get_urls(self):
        return [
           path('generate_description/<int:id>', self.generate_description, name="generate_description"),
        ] + super().get_urls()

    def _get_thumbnail(self, instance):
        return instance.filename if instance.filename.startswith("th_") else f"th_{instance.filename}"

    def _get_image(self, instance):
        return instance.filename.replace("th_", "")

    def generate_description(self, request, id):
        base_model = self.model.__name__.lower()
        base_tag_model = models.ImageTag if base_model == "image" else models.ThumbTag
        base_img_model = models.Image if base_model == "image" else models.Thumb
        instance = self.model.objects.get(id=id)
        thumbnail_file = ""
        for path in settings.STATICFILES_DIRS:
            test_path = f"{path}/{instance.video.base64_filename}/{self._get_thumbnail(instance)}"
            if os.path.exists(test_path):
                thumbnail_file = test_path

        if not os.path.exists(thumbnail_file):
            messages.error(request, f"Thumbnail file {thumbnail_file} does not exist.")
            return HttpResponseRedirect(f"/admin/videos/{base_model}/{id}/change/")

        try:
            description = utils.generate_description(thumbnail_file)

            instance.description = description["description"]
            instance.save()

            for tag in description["tags"]:
                tags_found = tags_models.Tag.objects.filter(slug=tag.lower().replace(" ", "-"))

                if tags_found:
                    obj = tags_found[0]
                else:
                    obj = tags_models.Tag.objects.create(text=tag)
                base_tag_model.objects.update_or_create(**{"tag": obj, base_model: instance})

        except Exception as e:
            messages.error(request, f"Error generating description: {e}")

        return HttpResponseRedirect(f"/admin/videos/{base_model}/{id}/change/")

    def show_thumbnail(self, instance):
        thumbnail_file = self._get_thumbnail(instance)
        image_file = self._get_image(instance)
        return format_html(
            '<a href="/static/{0}/{1}" target="_blank"><img src="/static/{0}/{2}" alt="{3}" style="border: none;"><a>',
            instance.video.base64_filename, image_file, thumbnail_file, instance.video.title)

    def show_description(self, instance):
        if instance.description:
            return instance.description
        else:
            return format_html(
                '<a href="/admin/videos/{0}/generate_description/{1}">Generate Description</a>',
                instance.__class__.__name__.lower(), instance.id)


@admin.register(models.Image)
class ImageAdmin(ShowThumbnailAdmin):
    inlines = [ImageTagInline, ]


@admin.register(models.Thumb)
class ThumbAdmin(ShowThumbnailAdmin):
    inlines = [ThumbTagInline, ]


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
