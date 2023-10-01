from django.urls.conf import path
from .views import MoviesViews, MovieDetailsViews, AddReview

urlpatterns = [
    path('', MoviesViews.as_view(), name='index'),
    path('<slug:slug>/', MovieDetailsViews.as_view(), name='movie_details'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]