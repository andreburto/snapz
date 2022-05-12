from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.LinkType)
class LinkTypeAdmin(admin.ModelAdmin):
    list_display = ('link_type', )
    ordering = ('link_type', )


@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_link', )
    ordering = ('title', 'url', )
