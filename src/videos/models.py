from django.contrib import admin
from django.db import models
from django.utils.html import format_html


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    base64_filename = models.TextField()

    class Meta:
        ordering = ["title", "filename", ]


    @admin.display()
    def video_url(self):
        return format_html(
            '<a href="/videos/video/{}/" target="_blank">View page</a>',
            self.id)

    def __str__(self):
        return self.title


class Image(models.Model):
    filename = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename
    

class Thumb(models.Model):
    filename = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

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
    ACTOR = 'Actor'
    DIRECTOR = 'Director'
    CHOICES = [
        (ACTOR, ACTOR, ),
        (DIRECTOR, DIRECTOR, ),
    ]
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=10, choices=CHOICES)

    @admin.display()
    def video_url(self):
        return format_html(
            '<a href="/videos/video/{}/" target="_blank">View page</a>',
            self.video.id)

    def __str__(self):
        return f"{self.video} with {self.person}"
