from django.shortcuts import render
from django.views.generic.base import View

from .models import Film


class MoviesView(View):

    def get(self, request):
        films = Film.objects.order_by('-id').all()
        return render(request, 'app_template/homepage.html', {'film_list': films})
    
class MoviesDetailView(View):

    def get(self, request, pk):
        movie = Film.objects.get(id=pk)
        return render(request, 'app_template/movie_detail.html', {'movie': movie})