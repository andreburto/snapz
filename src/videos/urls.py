from django.urls import path

from videos import views


urlpatterns = [
    path('', views.videos, name="videos"),
    path('video/<int:id>/', views.video, name="videos:video"),
]
