from . import views as news_views
from django.urls import path



app_name = 'news'
urlpatterns = [
    path('', news_views.MovieNewsList.as_view(), name='movie_news'),
    path('parse/', news_views.Parser, name="parse"),
    path('news_detail/<slug:url_news>/', news_views.NewsDetail.as_view(), name="news_detail"),
    path('news_detail/comment/<int:pk_article>/<int:pk_user>/', news_views.CommentView.as_view(), name="add_review"),
    # path('news_detail/delete_review/<int:pk_review>/<int:pk_article>', news_views.DeleteReview.as_view(), name="delete_review"),

    path('delete_review/', news_views.Delete_Review.as_view(), name="ajax_delete"),
    
]