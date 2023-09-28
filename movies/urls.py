from django.urls.conf import path
from .views import MoviesViews

urlpatterns = [
    path('', MoviesViews.as_view(), name='index')
]