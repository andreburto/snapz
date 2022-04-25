# snapz

## About

This is a Django+Docker+Bash project to help me catalog a collection of short videos.
It's not to be fancy. The choice was Python or C#, and Python won the coin toss.

## TODO

* Add height and width columns to Image and Thumb tables.
* Use [Pillow](https://pillow.readthedocs.io/en/stable/) to auto-grab image dimensions.
* Create permanent Dockerfile for the Django app.

## Change Log

**2022-04-24:** Restarted project with Docker Compose and Django. 
snapz will now extract screenshots, thumbnail them, and display a basic catalog with screencaps.

**2021-12-??:** Started project with a bash script to make snapshots from videos.
