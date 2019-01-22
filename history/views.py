from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Artist, Song

def index(request):
  all_artists = Artist.objects.all()
  context = {"all_artists": all_artists}
  return render(request, "history/index.html", context)


def detail(request, pk):
  songs = get_list_or_404(Song, ArtistId_id = pk)
  context = {"songs": songs}
  return render(request, "history/detail.html", context)
