from django.shortcuts import render
from django.views.generic.base import View

from .models import Film


class MoviesView(View):

    def get(self, request):
        films = Film.objects.all()

        return render(request, 'app_template/homepage.html', {'film_list': films})