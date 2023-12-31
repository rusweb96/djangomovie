from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie, Category, Actor
from .forms import ReviewForm


# Create your views here.
class MoviesViews(ListView):
    """ Логика показа Фильма """
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


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


class ActorView(DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'
