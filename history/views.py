from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song
from .forms import ArtistForm, SongForm

def index(request):
  all_artists = Artist.objects.all()
  context = {"all_artists": all_artists}
  return render(request, "history/artist.html", context)

def detail(request, pk):
  songs = get_list_or_404(Song, ArtistId_id = pk)
  artist = get_object_or_404(Artist, id = pk)
  context = {"songs": songs, "artist": artist}
  return render(request, "history/detail.html", context)

def addArtist(request):
  all_artists = Artist.objects.all()
  context = {"all_artists": all_artists}
  return render(request, "history/addArtist.html")

def save_artist(request):
  name = request.POST['artist_name']
  date = request.POST['artist_date']
  a = Artist(ArtistName = name, YearEstablished = int(date))
  a.save()
  response = redirect('/')
  return response

def addSong(request):
  return render(request, "history/addSong.html")

def submit_artist(request, name, date):
  context = {"name": name, "date": date}
  return render(request, 'history/newArtist.html', context)

