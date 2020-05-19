from django.shortcuts import render
from django.views.generic.base import View
from .models import ParseMovieInfo

import requests
from bs4 import BeautifulSoup as BS

# from datetime import datetime
# import locale

class MovieNewsList(View): #### парсить дание в когда час будет 13:00 или вроде того, идет проверка если интервал времени входит в 13:00 до 14:00 до парсит дание только один раз, нужно сделать доп. проверку
    def get(self, request):
        
        ###################################################### parser
        r = requests.get('https://www.kinonews.ru/news/') 
        html = BS(r.content, 'html.parser') 
        # now = datetime.now()
        # locale.setlocale(locale.LC_ALL, "ru")
        # print(now.strftime("%d %B %Y"))
        
        for el in html.select('.block-page-new'):
            title = el.select('.shiftup10 > .anons-title-new > h3 > a')
            dat = el.select('.shiftup10 > .anons-date-new')
            short_describe = el.select('.anons-text')
            url_more = el.select('.anons-readmore > a')
            break

        # full_describe = , source_link= ,
        news = ParseMovieInfo.objects.all()

        list_pages_link = []
        full_content_text = []
        for x in url_more:
            list_pages_link.append( requests.get('https://www.kinonews.ru/' + str(x.get('href'))) )
            
        
        for r in list_pages_link:
            full_text = ''
            html = BS(r.content, 'html.parser')
            for el in html.select('.textart'):
                full_content = el.select('div > p')

            for st in full_content:
                full_text += st.text + '\n\n'
            
            full_content_text.append(full_text)
            
        
        for iter in range(0,len(title)):
            T = True    
            for obj in news:
                if obj.title == title[iter].text:
                    T = False
            if T:
                ParseMovieInfo(
                    title = title[iter].text,
                    date = dat[iter].text, 
                    short_describe = short_describe[iter].text,
                    full_describe = full_content_text[iter], 
                    url = str(url_more[iter].get('href')).replace('/', '')
                ).save()
       
        ################################################## endpareser

        news_list = ParseMovieInfo.objects.order_by('-id').all()
    
        context = {
            'news_list': news_list,
        }
        return render(request, 'news_template/news.html', context)

class NewsDetail(View):
    def get(self, request, url_news):
        news = ParseMovieInfo.objects.get(url=url_news)
        
        context = {
            'news': news,
        }
        return render(request, 'news_template/news_detail.html', context)