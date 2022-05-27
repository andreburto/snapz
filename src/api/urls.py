from django.urls import path

from api import views


urlpatterns = [
    path('video/', views.video, name="api_video"),
    path('video/all/', views.video_all, name="api_video_all"),
    path('video/<int:id>/', views.video_one, name="api_video_one"),
    path('video/<int:id>/thumbnail/', views.video_thumbnails, name="api_video_thumbnails"),
]
