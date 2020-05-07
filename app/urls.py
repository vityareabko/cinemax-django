from . import views as app_views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', app_views.MoviesListView.as_view(), name = 'home'),
    path('movie_detail/<int:pk>/', app_views.MoviesDetailView.as_view(), name = "movie_detail"),
    path('actor/<int:pk>/', app_views.ActorDetailView.as_view(), name = "actor_detail" ),
    path('sessions/', app_views.SessionsListView.as_view(), name="sessions"),
    path('reserve/<int:pk_hall>/<int:pk_movie>/<int:pk_session>', app_views.ReserveListView.as_view(), name="reserve"),

    path('reservation_ticket/<int:pk_movie>/<int:pk_session>/<int:number_hall>/<int:pk_place>/<int:pk_sector>', app_views.ReservationView.as_view(), name = "reservation"),

    path('get_ticket/<int:pk_session>/<int:pk_place>/<int:total_sum>', app_views.ReserveDoneView.as_view(), name = 'get_ticket'),
]
# <int:pk_place>/<int:pk_sector>/<int:pk_session>
