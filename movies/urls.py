from django.urls.conf import path
from .views import MoviesViews, MovieDetailsViews

urlpatterns = [
    path('', MoviesViews.as_view(), name='index'),
    path('<slug:slug>/', MovieDetailsViews.as_view(), name='movie_details'),
]