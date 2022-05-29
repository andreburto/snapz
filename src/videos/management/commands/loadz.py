import os
import glob

from django.core.management.base import BaseCommand

from videos import models


class Command(BaseCommand):
    help = "Load images and video data into the database."

    def add_arguments(self, parser):
        parser.add_argument('--image', dest='image', action="store_true", default=False)
        parser.add_argument('--thumb', dest='thumb', action="store_true", default=False)
        parser.add_argument('--root-dir', dest='root_dir', required=True)
        parser.add_argument('--video', dest='video', action="store_true", default=False)
        parser.add_argument('--video-log', dest='video_log', default=False)

    def load_video(self, root_dir, video_log):
        all_videos = models.Video.objects.all()
        with open(video_log, "r") as fh:
            for i in fh.readlines():
                f, b = i.split("|")
                b = b.replace("\n", "")
                if all_videos.filter(filename=f, base64_filename=b).count() != 0:
                    continue
                v = models.Video.objects.create(title=f, filename=f, base64_filename=b)
                v.save()

    def load_image(self, root_dir, is_image, is_thumb):
        # For the recursive search below to work, the root_dir has to end with a slash.
        if not root_dir.endswith("/"):
            root_dir += "/"

        # This picks which model to load data into.
        picture_object = models.Image if is_image and not is_thumb else models.Thumb

        for filename in glob.iglob(root_dir + '*/*', recursive=True):
            print(f"filename: {filename}")
            if os.path.isdir(filename):
                continue

            parts = filename.split(os.path.sep)
            print(parts)
            base64_video = parts[-2]
            filename = parts[-1]

            try:
                video_record = models.Video.objects.get(base64_filename=base64_video)
            except:
                print(base64_video, filename)
                continue

            parameters = {
                "video": video_record,
                "filename": filename,
            }

            print(parameters)

            if is_thumb:
                image_file_name = filename.replace("th_", "")
                image_record = models.Image.objects.get(
                    filename=image_file_name,
                    video__base64_filename=base64_video)
                parameters.update({"image": image_record})

            picture_object.objects.update_or_create(**parameters)

    def handle(self, *args, **options):
        root_dir = options["root_dir"]
        video_log = options.get("video_log") or os.getenv("VIDEO_SUCCESS_LOG")
        is_image = options["image"]
        is_thumb = options["thumb"]
        is_video = options["video"]

        if is_image == is_thumb == is_video:
            raise ValueError("You must choose only one of the parameters: --image, --thumb, --video.")

        if is_video:
            self.load_video(root_dir, video_log)
        else:
            self.load_image(root_dir, is_image, is_thumb)
