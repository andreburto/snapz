from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from . import models


def videos(request):
    video_list = models.Video.objects.all()
    return HttpResponse(render_to_string(
        "videos/videos.html",
        {
            'video_list': video_list,
        }))


def video(request, id):
    select_video = models.Video.objects.get(id=id)
    return HttpResponse(render_to_string(
        "videos/video.html",
        {
            'video_title': select_video.title,
        }))
