# snapz

## About

This is a Django+Docker+Bash project to help me catalog a collection of short videos.
It's not to be fancy. The choice was Python or C#, and Python won the coin toss.

## To Do

* Add height and width columns to Image and Thumb tables.
* Use [Pillow](https://pillow.readthedocs.io/en/stable/) to auto-grab image dimensions.

## Change Log

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
