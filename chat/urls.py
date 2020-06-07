from . import views as chat_views
from django.urls import path


app_name = 'chat'
urlpatterns = [
    path('', chat_views.ListChat.as_view(), name='chat_list')

]