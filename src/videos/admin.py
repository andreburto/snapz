from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Thumb)
class ThumbAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VideoPeople)
class VideoPeopleAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'person_fullname', 'role', )

    def video_title(self, instance):
        return instance.video

    def person_fullname(self, instance):
        return f"{instance.person.last_name}, {instance.person.first_name}"
