from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import ReviewForm


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
