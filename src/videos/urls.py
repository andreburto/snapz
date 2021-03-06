from django.urls import path

from videos import views


urlpatterns = [
    path('', views.videos, name="videos"),
    path('video/<int:id>/', views.video, name="video"),
    path('tag/<str:slug>/', views.video_by_tag, name="video_by_tag"),
    path('people/', views.people, name="people"),
    path('person/<int:id>/', views.person, name="person"),
]
