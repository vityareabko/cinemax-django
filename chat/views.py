from django.shortcuts import render

from django.views.generic.base import View


class ListChat(View):
    def get(self,request):
        ctx = {}
        return render(request, 'chat_template/list_chat.html')