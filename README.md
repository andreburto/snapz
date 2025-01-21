# snapz

## About

This is a Django+Docker+Bash project to help me catalog a collection of short videos.
It's not to be fancy. The choice was Python or C#, and Python won the coin toss.

## Usage

All of the following assume you are in the root project directory, where `docker-compose.yml` lives.
All assume you have Docker running and an `.env` file with the proper values.

Example `.env` file:
```
DATABASE_PATH=/app/data/snapz.db
VIDEO_PATH=/path/to/videos
VIDEO_SUCCESS_LOG=/app/data/video_success_log.txt
```

### snapz

Generates screencaps in the `images` directory.

`docker-compose run ffmpeg`

### thumbz

Generates screencap thumbnails in the `thumbs` directory.

`docker-compose run imagemagick`

### loadz

Loads video, image, and thumbnail data from filesystem sources into the database

`docker-compose run loadz`

### pagez

Runs the web app database.

`docker-compose run --service-ports pagez`

## To Do

* **Data management**
  * General search system.
  * Add tags to people.
  * Clone RDB (SQLite) to NoSQL (DynamoBD) for backups.
  * Filter out videos that already have images and thumbnails.
* **Media management**
  * Use [Pillow](https://pillow.readthedocs.io/en/stable/) to auto-grab image dimensions.
  * Add height and width columns to Image and Thumb tables.
  * Uploading files.
* **UI improvements**
  * JSON endpoints with [DRF](https://www.django-rest-framework.org/).
  * Create tag cloud.
* **Infrastructure**
  * Add linter and tests.
  * Startup scripts for Windows and Mac.


## Change Log

**2025-01-20:** Started working on basic integration with [OpenAI](https://www.openai.com/) to help describe screenshots.
Added the `terraform` directory that adds the S3 bucket to make it easier to hand images to ChatGPT.
The description code works, but there is a bug where some images are not found in the STATIC_ROOT directory.

**2022-07-30:** Added description to video page.

**2022-06-11:** Correcting errors in usage section of README.

**2022-05-29:** Field tested loading new data after many app changes, made corrections accordingly.
Updated this file with usage instructions.
Updated `loadz.py` to load video data.

**2022-05-23:** Added Api app and created a few JSON endpoints.
Need to find a better method than handcrafted JSON.

**2022-05-22:** Added thumbnails to the Image admin page using a base ShowThumnbailAdmin class.

**2022-05-21:** Added InLine field on Video admin page for editing Tags.
Added tags to video page, and created page to show videos by tag.
Improved To Do list above.

**2022-05-19:** Added a few indexes to tables.
Created Tags and Tools apps.

**2022-05-16:** Fixed previous date.
Started working with uploading files.

**2022-05-15:** Added Studio tables.
The save logic still needs some work.
Added description field to videos.
Tinkered with the people display page.

**2022-05-11:** Added `linkz` app and all of its initial parts.
Sort main video list without case sensitivity.

**2022-05-08:** Updated Image and Thumb tables by renaming `filename` field.
Added thumbnail image to Person record.
Cleaned up Docker settings.
Set order to some admin forms.

**2022-05-07:** Added People and Person pages.
Created Dockerfile to speed up starting the app.
Generalized templates to reduce duplicate code.

**2022-04-24:** Restarted project with Docker Compose and Django. 
snapz will now extract screenshots, thumbnail them, and display a basic catalog with screencaps.

**2021-12-??:** Started project with a bash script to make snapshots from videos.
