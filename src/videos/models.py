from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from linkz import models as linkz_models
from tags import models as tags_models


# Create your models here.
class Video(linkz_models.DescriptionMixin):
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    base64_filename = models.TextField()
    studio = models.ForeignKey("Studio", on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['filename', ]),
        ]
        ordering = ["title", "filename", ]

    @admin.display()
    def video_url(self):
        return format_html('<a href="/videos/video/{}/" target="_blank">View page</a>', self.id)

    def __str__(self):
        return self.title


class Image(models.Model):
    filename = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['video', ]),
        ]
        ordering = ["video__title", "filename", ]

    def __str__(self):
        return self.filename
    

class Thumb(models.Model):
    filename = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['video', ]),
        ]
        ordering = ["video__title", "filename", ]

    @admin.display()
    def show_thumbnail(self):
        return format_html(
            '<img src="/static/{}/{}" alt="{}">',
            self.video.base64_filename, self.filename, self.video.title)

    def __str__(self):
        return f"{self.video.title} - {self.filename}"


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    thumb = models.ForeignKey(Thumb, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name", ]

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class VideoPeople(models.Model):
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, blank=True, null=True)
    ACTOR = 'Actor'
    DIRECTOR = 'Director'
    CHOICES = [
        (ACTOR, ACTOR, ),
        (DIRECTOR, DIRECTOR, ),
    ]
    role = models.CharField(max_length=10, choices=CHOICES)

    @admin.display()
    def video_url(self):
        return format_html('<a href="/videos/video/{}/" target="_blank">View page</a>', self.video.id)

    def __str__(self):
        return f"{self.video} with {self.person}"


class LinkPeople(models.Model):
    link = models.ForeignKey(linkz_models.Link, on_delete=models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.person} @ {self.link.link_type}"


class StudioName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Studio(models.Model):
    studio_name = models.ForeignKey(StudioName, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=1024, blank=True, null=True)
    website = models.ForeignKey(linkz_models.Link, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.studio_name.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        StudioNameStudio.objects.filter(studio_id=self.id).update(current=False)
        StudioNameStudio.objects.update_or_create(studio_id=self.id, studio_name_id=self.studio_name.id)
        StudioNameStudio.objects.filter(studio_id=self.id, studio_name_id=self.studio_name.id).update(current=True)


class StudioNameStudio(models.Model):
    studio_name = models.ForeignKey(StudioName, on_delete=models.DO_NOTHING)
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING)
    current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.studio_name.name}"


class VideoTag(models.Model):
    tag = models.ForeignKey(tags_models.Tag, on_delete=models.DO_NOTHING, unique=True)
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['tag', ]),
            models.Index(fields=['video', ]),
            models.Index(fields=['tag', 'video', ]),
        ]
        ordering = ['video', 'tag', ]
