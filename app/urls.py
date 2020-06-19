from . import views as app_views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', app_views.MoviesListView.as_view(), name = 'home'),
    # path('me_account', app_views.AccountChange.as_view(), name="me_account"),
    path('movie_detail/<int:pk>/', app_views.MoviesDetailView.as_view(), name = "movie_detail"),
    
    path('actor/<int:pk>/', app_views.ActorDetailView.as_view(), name = "actor_detail" ),
    path('sessions/', app_views.SessionsListView.as_view(), name="sessions"),
    path('reserve/<int:pk_hall>/<int:pk_movie>/<int:pk_session>', app_views.ReserveListView.as_view(), name="reserve"),
    path('reservation_ticket/<int:pk_movie>/<int:pk_session>/<int:number_hall>/<int:pk_place>/<int:pk_sector>', app_views.ReservationView.as_view(), name = "reservation"),
    path('get_ticket/<int:pk_session>/<int:pk_place>/<int:total_sum>/<str:email>', app_views.ReserveDoneView.as_view(), name = 'get_ticket'),
    path('movie_detail/add_comment/<int:pk_movie>/<int:pk_user>', app_views.MovieListComments.as_view(), name="movie_comment"),
    path('update_review/', app_views.UpdateReview.as_view(), name="update_review"),
    path('delete_review/', app_views.Delete_Review.as_view(), name="ajax_delete"),

    path('liked_review/', app_views.Liked_Review.as_view(), name="liked_review"),
    path('dislike_review/', app_views.Dislike_Review.as_view(), name="dislike_review"),
    
    path('thanks/', app_views.ThankPage.as_view(), name="thank_page")
    
    
]
# <int:pk_place>/<int:pk_sector>/<int:pk_session>
