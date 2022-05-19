from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("text", "slug", "description", )
    fields = ["text", "slug", "description", ]
    ordering = ("text", )
    readonly_fields = ("slug", )
