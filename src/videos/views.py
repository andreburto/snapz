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
    video_image_list = models.Image.objects.filter(video=select_video)
    video_thumb_list = models.Thumb.objects.filter(video=select_video)
    starring_people = models.Person.objects.filter(
        id__in=models.VideoPeople.objects.filter(video=select_video).values_list('person__id', flat=True))

    print(starring_people)

    image_and_thumb_list = [
        {
            "image": i.file_name,
            "thumb": video_thumb_list.filter(image=i).first().file_name
        }
        for i in list(video_image_list)
    ]

    return HttpResponse(render_to_string(
        "videos/video.html",
        {
            'video_title': select_video.title,
            'base64_filename': select_video.base64_filename,
            'image_and_thumb_list': image_and_thumb_list,
            'starring_people': starring_people,
        }))
