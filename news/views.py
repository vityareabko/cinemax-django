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
            tit_en = trans.translate(title[iter].text, src = 'ru', dest='en').text
            if obj.title == tit or obj.title == tit_en:
                T = False
        if T:
            tit = trans.translate(title[iter].text, src = 'ru', dest='uk').text
            tit_en = trans.translate(title[iter].text, src = 'ru', dest='en').text
            sh_d = trans.translate(short_describe[iter].text, src = 'ru', dest='uk').text
            sh_d_en = trans.translate(short_describe[iter].text, src = 'ru', dest='en').text
            full_d = trans.translate(full_content_text[iter], src = 'ru', dest='uk').text
            full_d_en = trans.translate(full_content_text[iter], src = 'ru', dest='en').text
            ParseMovieInfo(
                title = tit,
                title_uk = tit,
                title_en = tit_en,
                date = dat[iter].text, 
                short_describe = sh_d,
                short_describe_uk = sh_d,
                short_describe_en = sh_d_en,
                full_describe = full_d, 
                full_describe_uk = full_d, 
                full_describe_en = full_d_en, 
                url = str(url_more[iter].get('href')).replace('/', '')
            ).save()
    
    return HttpResponseRedirect( reverse('news:movie_news', args=()))
    ################################################## endpareser
from django.core.paginator import Paginator
from django.views.generic import ListView
class MovieNewsList(ListView): #### парсить дание в когда час будет 13:00 или вроде того, идет проверка если интервал времени входит в 13:00 до 14:00 до парсит дание только один раз, нужно сделать доп. проверку
    model = ParseMovieInfo
    # context_object_name = 'posts'
    template_name = 'news_template/news.html'
    paginate_by = 5
    
    # def get(self, request):
    #     news_list = ParseMovieInfo.objects.order_by('-id').all()
    #     current_page = Paginator(news_list,6)
    #     context = {
    #         'news_list': current_page.page(page_number),
            
    #     }
    #     return render(request, 'news_template/news.html', context)

class NewsDetail(View):
    def get(self, request, url_news):
        news = ParseMovieInfo.objects.get(url=url_news)
        news_list = ParseMovieInfo.objects.order_by('-id').all()
        comments = ArticleComment.objects.order_by('-id').filter(id_article_id = news.id, id_parent_id = None)
        comments_r = ArticleComment.objects.filter(id_article_id = news.id, id_parent_id__isnull=False)
        print(len(comments_r))
        quantity = len(comments)      
       
        context = {
            'news': news,
            'news_list': news_list,
            'comments': comments,
            'comments_r': comments_r,
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
            if request.POST.get('parent'):
                ArticleComment(comment = message, id_user_id = pk_user, id_article_id = pk_article, id_parent_id = request.POST.get('parent')).save()
            else:
                ArticleComment(comment = message, id_user_id = pk_user, id_article_id = pk_article).save()
            
            id_comment = ArticleComment.objects.order_by('-id').filter(comment=message, id_user_id = pk_user)

            data = {
                'count_liked': id_comment[0].liked.all().count(),
                'count_dislike': id_comment[0].dislike.all().count(),
                
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


class Liked_Review(View):
    def get(self, request):
        user = request.user
        # print(request.GET.get('id_article'))
        # print(request.GET.get('id_review'))

        review = ArticleComment.objects.get(id = request.GET.get('id_review'))

        if user not in review.liked.all():
            if user in review.dislike.all():
                review.dislike.remove(user)
                # data['like'] = True # тут пользователь біл в лайках и мы его удалили из лайком и поэтому труе - потому что нужно изминить в шаблоне (убрать этот лайк)

            review.liked.add(user)
            
            # data['dislike'] = True # труе потому что нам нужно добавить измениния в дизлайков 
        else:
            review.liked.remove(user)

        if user in review.liked.all():
            user_liked = True
        else:
            user_liked = False

        data={
            'id_review': request.GET.get('id_review'),
            'count_like': review.liked.all().count(),
            'conut_dislike': review.dislike.all().count(),
            'user_liked': user_liked,
        }
        
        
        print(data)
        return JsonResponse(data)


class Dislike_Review(View):
    def get(self, request):
        user = request.user

        review = ArticleComment.objects.get(id = request.GET.get('id_review'))
        if user not in review.dislike.all():
            if user in review.liked.all():
                review.liked.remove(user)
                # data['like'] = True # тут пользователь біл в лайках и мы его удалили из лайком и поэтому труе - потому что нужно изминить в шаблоне (убрать этот лайк)

            review.dislike.add(user)
            
            # data['dislike'] = True # труе потому что нам нужно добавить измениния в дизлайков 
        else:
            review.dislike.remove(user)

        if user in review.dislike.all():
            user_disliked = True
        else:
            user_disliked = False

        data={
            'id_review': request.GET.get('id_review'),
            'count_like': review.liked.all().count(),
            'conut_dislike': review.dislike.all().count(),
            'user_dislike': user_disliked,
        }
        
        print(data)
        return JsonResponse(data)