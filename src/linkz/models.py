from django.contrib import admin
from django.db import models
from django.utils.html import format_html


class DescriptionMixin(models.Model):
    description = models.TextField(max_length=1024, blank=True, null=True)

    class Meta:
        abstract = True


# Create your models here.
class LinkType(DescriptionMixin):
    link_type = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.link_type


class Link(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    link_type = models.ForeignKey(LinkType, on_delete=models.DO_NOTHING)

    @admin.display()
    def show_link(self):
        return format_html('<a href="{}" target="_blank">{}</a>', self.url, self.title)

    def __str__(self):
        return f"Url: {self.url}, Title: {self.title}"

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = str(self.url)
        super().save(*args, **kwargs)
