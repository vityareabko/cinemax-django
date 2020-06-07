from . import views as notifi_views
from django.urls import path

urlpatterns = [
     path('', notifi_views.NotificationList.as_view(), name = 'notification'),
]
