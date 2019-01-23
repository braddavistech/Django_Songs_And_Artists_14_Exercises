from django import forms
from .models import Artist, Song

class ArtistForm(forms.ModelForm):

  class Meta:
      model = Artist
      fields = ('ArtistName', 'YearEstablished')



class SongForm(forms.ModelForm):

  class Meta:
      model = Song
      fields = ('Title', 'SongLength', 'ReleaseDate', 'Genre', 'Art', 'Video')