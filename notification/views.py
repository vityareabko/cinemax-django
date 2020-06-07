from django.shortcuts import render
from django.views.generic.base import View

class NotificationList(View):
    def get(self,request):
        ctx = {

        }
        return render(request, 'notifi_template/notification.html', ctx)

