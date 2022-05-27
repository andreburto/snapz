from django.db.models.functions import Lower
from django.http import HttpResponseRedirect, JsonResponse

from videos import models as video_models


def video(request):
    return HttpResponseRedirect("/api/v1/video/all", status=301)


def video_all(request):
    videos = video_models.Video.objects.all().values("id", "description", "title").order_by(Lower("title"))
    return JsonResponse({"videos": list(videos)}, safe=False)


def video_one(request, id):
    video = video_models.Video.objects.filter(id=id).values()
    return JsonResponse({"video": video}, safe=False)


def video_thumbnails(request, id):
    video_record = video_models.Video.objects.filter(id=id).values("id", "base64_filename").first()
    thumbnails = video_models.Thumb.objects.filter(video_id=id)
    thumbnail_files = sorted([t.filename for t in list(thumbnails)],
                              key=lambda x: int(x.replace("th_", "").split(".")[0]))
    return JsonResponse({"video": video_record, "thumbnails": thumbnail_files, })
