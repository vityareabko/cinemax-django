from . import views as news_views
from django.urls import path

app_name = 'news'
urlpatterns = [
    path('', news_views.MovieNewsList.as_view(), name='movie_news')
]