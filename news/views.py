from django.shortcuts import render
from django.views.generic.base import View

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import ParseMovieInfo, ArticleComment
from .forms import ArticleCommentForm

import requests
from bs4 import BeautifulSoup as BS

# from datetime import datetime
# import locale
from googletrans import Translator

def Parser(request):
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
        
    
    
    trans = Translator()
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
            tit = trans.translate(title[iter].text, src = 'ru', dest='uk').text
            if obj.title == tit:
                T = False
        if T:
            tit = trans.translate(title[iter].text, src = 'ru', dest='uk').text
            sh_d = trans.translate(short_describe[iter].text, src = 'ru', dest='uk').text
            full_d = trans.translate(full_content_text[iter], src = 'ru', dest='uk').text
            ParseMovieInfo(
                title = tit,
                date = dat[iter].text, 
                short_describe = sh_d,
                full_describe = full_d, 
                url = str(url_more[iter].get('href')).replace('/', '')
            ).save()
    
    return HttpResponseRedirect( reverse('news:movie_news', args=()))
    ################################################## endpareser

class MovieNewsList(View): #### парсить дание в когда час будет 13:00 или вроде того, идет проверка если интервал времени входит в 13:00 до 14:00 до парсит дание только один раз, нужно сделать доп. проверку
    def get(self, request):
        
        

        news_list = ParseMovieInfo.objects.order_by('-id').all()
    
        context = {
            'news_list': news_list,
        }
        return render(request, 'news_template/news.html', context)

class NewsDetail(View):
    def get(self, request, url_news):
        news = ParseMovieInfo.objects.get(url=url_news)
        news_list = ParseMovieInfo.objects.order_by('-id').all()
        comments = ArticleComment.objects.order_by('-id').filter(id_article_id = news.id, id_parent_id = None)
        reply_comments = ArticleComment.objects.order_by('-id').filter(id_parent_id = not None)
        # print(len(comments.count))
        quantity = len(comments)
        
        context = {
            'news': news,
            'news_list': news_list,
            'comments': comments,
            'reply_comments': reply_comments,
            'quantity': quantity
        }
        return render(request, 'news_template/news_detail.html', context)

#############################################
from django.http import JsonResponse

def AjaxReview(request):
    data = {
            'is_valid': False,
    }
    
    # slug_url_article = ParseMovieInfo.objects.get(id=pk_article).url
    if request.is_ajax():
        print('\n\n1\n\n')
        message = request.GET.get('comment')
        data['comment'] = message
        if message == 'I want an AJAX response':
            print('###'+message)
            data.update(is_valid=True)

            

            # form = ArticleCommentForm(request.POST)
            # if form.is_valid():
            #     form = form.save(commit=False)
            #     if request.POST.get("parent", None):
            #         form.id_parent_id = int(request.POST.get("parent"))
            #     form.id_article_id = pk_article
            #     form.id_user_id = pk_user
            #     form.save()
            

    return JsonResponse(data)


############################################


class CommentView(View):
    def post(self, request, pk_article, pk_user):
        # comment = request.POST['comment']
        # # print(comment)
        # ArticleComment(comment = comment, id_user_id = pk_user, id_article_id = pk_article).save()
        slug_url_article = ParseMovieInfo.objects.get(id=pk_article).url
        
        if request.is_ajax():
            
            message = request.POST.get('comment')
            data = {
                'comment': message
            }
            form = ArticleCommentForm(request.POST)
            if form.is_valid():
    
                form = form.save(commit=False)
                if request.POST.get("parent", None):
                    form.id_parent_id = int(request.POST.get("parent"))
                form.id_article_id = pk_article
                form.id_user_id = pk_user
                form.save()
        
                print('###'+message)
                return JsonResponse(data)

        return HttpResponseRedirect( reverse('news:news_detail', args=(slug_url_article,)))