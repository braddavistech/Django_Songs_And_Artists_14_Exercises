from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('addArtist', views.addArtist, name='addArtist'),
    path('addSong', views.addSong, name='addSong'),
    path('newArtist', views.submit_artist, name='submit_artist'),
     path('saveArtist', views.save_artist, name='save_artist'),
]