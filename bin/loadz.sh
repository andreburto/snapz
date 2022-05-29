#!/bin/bash

. /root/venv/bin/activate

cd /app/src

# Load order: Video -> Image -> Thumb
echo "LOADING VIDEOS"
python3 manage.py loadz --video --root-dir /app/videos

echo "LOADING IMAGES"
python3 manage.py loadz --image --root-dir /app/images

echo "LOADING THUMBNAILS"
python3 manage.py loadz --thumb --root-dir /app/thumbs
