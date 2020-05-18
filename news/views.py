from django.shortcuts import render
from django.views.generic.base import View
from .models import ParseMovieInfo


# from datetime import datetime
# import locale

class MovieNewsList(View): #### парсить дание в когда час будет 13:00 или вроде того, идет проверка если интервал времени входит в 13:00 до 14:00 до парсит дание только один раз, нужно сделать доп. проверку
    def get(self, request):
        
        
        news_list = ParseMovieInfo.objects.all()
    
        context = {
            'news_list': news_list,
        }
        return render(request, 'news_template/news.html', context)
