from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie


# Create your views here.
class MoviesViews(ListView):
    """ Логика показа Фильма """
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


class MovieDetailsViews(DetailView):
    """ Логика Детального описание фильма """
    model = Movie
    slug_field = 'url'
    template_name = 'movies/Movie_detail.html'
