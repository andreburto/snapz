from django.urls import path

from videos import views


urlpatterns = [
    path('', views.videos, name="videos"),
    path('video/<int:id>/', views.video, name="video"),
    path('people/', views.people, name="people"),
    path('person/<int:id>/', views.person, name="person"),
]
