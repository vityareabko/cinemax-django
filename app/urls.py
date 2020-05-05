from . import views as app_views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', app_views.MoviesListView.as_view(), name = 'home'),
    path('movie_detail/<int:pk>/', app_views.MoviesDetailView.as_view(), name = "movie_detail"),
    path('sessions/', app_views.SessionsListView.as_view(), name="sessions"),
    path('reserve/<int:pk_hall>/<int:pk_movie>/<int:pk_session>', app_views.ReserveListView.as_view(), name="reserve"),
]
