import os
import glob

from django.core.management.base import BaseCommand, CommandError

from videos import models


class Command(BaseCommand):
    help = 'Create an admin user by simply providing a password.'

    def add_arguments(self, parser):
        parser.add_argument('--image', dest='image', action="store_true", default=False)
        parser.add_argument('--thumb', dest='thumb', action="store_true", default=False)
        parser.add_argument('--root-dir', dest='root_dir', required=True)

    def handle(self, *args, **options):
        root_dir = options["root_dir"]
        is_image = options["image"]
        is_thumb = options["thumb"]

        picture_object = models.Image if is_image and not is_thumb else models.Thumb

        for filename in glob.iglob(root_dir + '*/*', recursive=True):
            if os.path.isdir(filename):
                continue

            parts = filename.split(os.path.sep)
            base64_video = parts[-2]
            filename = parts[-1]

            video_record = models.Video.objects.get(base64_filename=base64_video)

            parameters = {
                "video": video_record,
                "file_name": filename,
            }

            if is_thumb:
                image_file_name = filename.replace("th_", "")
                image_record = models.Image.objects.get(
                    file_name=image_file_name,
                    video__base64_filename=base64_video)
                parameters.update({"image": image_record})

            picture_object.objects.update_or_create(**parameters)
