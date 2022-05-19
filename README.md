# snapz

## About

This is a Django+Docker+Bash project to help me catalog a collection of short videos.
It's not to be fancy. The choice was Python or C#, and Python won the coin toss.

## To Do

* Add height and width columns to Image and Thumb tables.
* Use [Pillow](https://pillow.readthedocs.io/en/stable/) to auto-grab image dimensions.
* Tags field for videos.
* Index tables better.
* Uploading files.

## Change Log

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
