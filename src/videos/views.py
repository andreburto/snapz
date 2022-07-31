from django.conf import settings
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.template.loader import render_to_string

from tags import models as tag_models
from . import models


def videos(request):
    video_list = models.Video.objects.all().order_by(Lower("title"))
    return HttpResponse(render_to_string(
        "videos/videos.html",
        {
            'video_list': video_list,
        }))


def video(request, id):
    select_video = models.Video.objects.get(id=id)
    video_image_qs = models.Image.objects.filter(video=select_video)
    video_thumb_qs = models.Thumb.objects.filter(video=select_video)
    starring_people = models.Person.objects.filter(
        id__in=models.VideoPeople.objects.filter(video=select_video).values_list('person__id', flat=True))
    tags_for_video = models.VideoTag.objects.filter(video=select_video).order_by('tag__slug')

    # Images are named as numbers plus extensions (1.png), so cannot be easily sorted with the ORM.
    # This will sort them by transforming the file name into an integer.
    image_and_thumb_list = sorted([
            {
                "image": i.filename,
                "thumb": video_thumb_qs.filter(image=i).first().filename
            }
            for i in list(video_image_qs)
        ],
        key=lambda image: int(image["image"].split(".")[0]))

    return HttpResponse(render_to_string(
        "videos/video.html",
        {
            'video_id': select_video.id,
            'video_title': select_video.title,
            'video_description': select_video.description,
            'video_filename': select_video.filename,
            'base64_filename': select_video.base64_filename,
            'image_and_thumb_list': image_and_thumb_list,
            'starring_people': starring_people,
            'tags_for_video': list(tags_for_video),
        }))


def people(request):
    people_list = models.Person.objects.all().order_by("last_name", "first_name")
    people_table = []
    for idx in range(0, len(people_list), settings.MAX_COLS_FOR_PEOPLE):
        people_table.append(people_list[idx:idx+settings.MAX_COLS_FOR_PEOPLE])

    return HttpResponse(render_to_string("videos/people.html", {'people_table': people_table, }))


def person(request, id):
    p = models.Person.objects.get(id=id)
    video_id_by_person = models.VideoPeople.objects.filter(person=p).values_list('video__id', flat=True)
    videos_with_person = models.Video.objects.filter(id__in=video_id_by_person).order_by(Lower("title"))
    links_for_people = list(models.LinkPeople.objects.filter(person=p))

    if getattr(p, 'thumb', None):
        thumb_url = f"/static/{p.thumb.video.base64_filename}/{p.thumb.filename}"
    else:
        thumb_url = None

    return HttpResponse(render_to_string(
        "videos/person.html",
        {
            "person_id": p.id,
            "first_name": p.first_name,
            "last_name": p.last_name,
            "thumb_url": thumb_url,
            "link_list": links_for_people,
            "video_list": videos_with_person,
        }))


def video_by_tag(request, slug):
    tag = tag_models.Tag.objects.filter(slug=slug).first()
    videos_with_tag = models.Video.objects.filter(
        id__in=models.VideoTag.objects.filter(tag=tag).values_list("video__id")).order_by("title")

    return HttpResponse(render_to_string(
        "videos/videos_by_tag.html",
        {
            "tag": tag,
            "video_list": videos_with_tag,
        }))
