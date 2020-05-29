from django.shortcuts import render
from django.views.generic.base import View

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import ParseMovieInfo, ArticleComment
# from .forms import ArticleCommentForm

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
        comments = ArticleComment.objects.order_by('-id').filter(id_article_id = news.id)
        # print(len(comments.count))
        quantity = len(comments)      
        
        context = {
            'news': news,
            'news_list': news_list,
            'comments': comments,
            'quantity': quantity,

        }
        return render(request, 'news_template/news_detail.html', context)


class CommentArticleView(View):
    def post(self, request, pk_article, pk_user):
        # comment = request.POST['comment']
        # # print(comment)
        # ArticleComment(comment = comment, id_user_id = pk_user, id_article_id = pk_article).save()
        slug_url_article = ParseMovieInfo.objects.get(id=pk_article).url
        
     
        if request.is_ajax():
            
            message = request.POST.get('comment') #

            ArticleComment(comment = message, id_user_id = pk_user, id_article_id = pk_article).save()


            id_comment = ArticleComment.objects.order_by('-id').filter(comment=message, id_user_id = pk_user)
            data = {
                'id_comment': int(id_comment[0].id),
                'comment': message,
               
            }
                
            
    
            print('###'+message)
            return JsonResponse(data)
            

        return HttpResponseRedirect( reverse('news:news_detail', args=(slug_url_article,)))

# class DeleteReview(View):

#     def get(self, request, pk_review, pk_article):
#         slug_url_article = ParseMovieInfo.objects.get(id=pk_article).url

#         ArticleComment.objects.get(id = pk_review).delete()

#         return HttpResponseRedirect( reverse('news:news_detail', args=(slug_url_article,)))




class Delete_Review(View):
    def get(self, request):
        id_review = request.GET.get('id_review', None)
        ArticleComment.objects.get(id = id_review).delete()

        data = {
            'deleted': True,
        }
        return JsonResponse(data)

class UpdateReview(View):
    def post(self, request):
        message_edited = request.POST.get('review_edited');
        id_review = request.POST.get('id_review');
        update_review = ArticleComment.objects.get(id = id_review)
        update_review.comment = message_edited
        update_review.save()
        data = {
            'id_review': id_review,
            'review_edited': message_edited,
        }
        print(data)
        return JsonResponse(data)

class Liked_Article(View):
    def get(self, request):
        user = request.user
        

        id_article = request.GET.get('id_article')
        article_like_upd = ParseMovieInfo.objects.get(id = id_article)
        
        if user not in article_like_upd.liked.all(): 
            if user in article_like_upd.dislike.all():
                article_like_upd.dislike.remove(user)

            article_like_upd.liked.add(user)

        else:
            article_like_upd.liked.remove(user)
     
        # print(article_like_upd.liked.all().count())
        # print(article_like_upd.dislike.all().count())
        if user in article_like_upd.liked.all():
            user_liked = True
        else:
            user_liked = False

        data={
            'count_like': article_like_upd.liked.all().count(),
            'conut_dislike': article_like_upd.dislike.all().count(),
            'user_liked': user_liked
        }
        print(data)
        
        return JsonResponse(data)

class Dislike_Article(View):
    def get(self, request):
        

        user = request.user
        id_article = request.GET.get('id_article')
        article_dislike_upd = ParseMovieInfo.objects.get(id = id_article)

      
        if user not in article_dislike_upd.dislike.all():
            if user in article_dislike_upd.liked.all():
                article_dislike_upd.liked.remove(user)
                # data['like'] = True # тут пользователь біл в лайках и мы его удалили из лайком и поэтому труе - потому что нужно изминить в шаблоне (убрать этот лайк)

            article_dislike_upd.dislike.add(user)
            
            # data['dislike'] = True # труе потому что нам нужно добавить измениния в дизлайков 
        else:
            article_dislike_upd.dislike.remove(user)
            # data['not_dislike'] = True # труе потому что мы просто хотим убрать лайк и все

        if user in article_dislike_upd.dislike.all():
            user_disliked = True
        else:
            user_disliked = False

        data={
            'count_like': article_dislike_upd.liked.all().count(),
            'conut_dislike': article_dislike_upd.dislike.all().count(),
            'user_dislike': user_disliked,
        }
        print(data)

        
        return JsonResponse(data)