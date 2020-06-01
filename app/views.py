from django.shortcuts import render
from django.views.generic.base import View
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.core.mail import send_mail

from .models import Film, Actor, Session, Time_Sessions, Hall, Place, Sector, Ticket, Weekday, Comments
from news.models import ParseMovieInfo
from datetime import datetime, date, time
import datetime
import random

class MoviesListView(View):

    # model = Film
    # queryset = Film.objects.order_by('-id').all()
    # context_object_name = "film_list"
    # template_name = "app_template/homepage.html"
    def get(self, request):
        
    
        



        movie = Film.objects.order_by('-id').all()
        
        count_movie = 0
        for i in movie:
            count_movie += 1
        movie_hero = Film.objects.get(id = random.randint(1, count_movie))

        context = {
            'film_list': movie,
            'movie_hero': movie_hero,
        }

        return render(request, 'app_template/homepage.html', context)
    
class MoviesDetailView(View):

    # model = Film
    # context_object_name = "movie"
    # template_name = "app_template/movie_detail.html"
    
   
    def get(self, request, pk):
        movie = Film.objects.get(id=pk)
        comments = Comments.objects.order_by('-id').filter(id_film_id=pk)
        comments_r = Comments.objects.filter(id_film_id = movie.id, id_parent_id__isnull=False)
        article = ParseMovieInfo.objects.order_by('-id').all()
        context = {
            'movie': movie,
            'comments': comments,
            'comments_r': comments_r,
            'article': article,
        }
        return render(request, 'app_template/movie_detail.html', context)

class ActorDetailView(View):

    def get(self, request, pk):
        actor = Actor.objects.get(id=pk) 
        context = {
            'actor': actor,
        }
        return render(request, 'app_template/actor_detail.html', context)

class SessionsListView(View):
    
    def get(self, request):
        tday = date.today()
        num_week_day = date.today().weekday()
        sessions = Session.objects.all()

        ##########################################################
        days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'нд']
        k = 0
        ################################################################################ - баги на сервере может быть потому что этот кусок кода удаляет из таблицы даные и записывает их снова и снова
        # Weekday.objects.all().delete()
        for i in range(0, len(days)):
            try:
                Weekday.objects.filter(weekday = days[num_week_day + i]).update(date = tday + datetime.timedelta(days=i))
                # Weekday(weekday = days[num_week_day + i], date = tday + datetime.timedelta(days=i)).save()
                k += 1
            except Exception:
                Weekday.objects.filter(weekday = days[i-k]).update(date = tday + datetime.timedelta(days=i))
                # Weekday(weekday = days[i-k], date = tday + datetime.timedelta(days=i)).save()
        
        active_vkladka = 0
        for day in Weekday.objects.all():
            dat = day.date
            if dat.weekday() == num_week_day:
                active_vkladka = day.weekday_en

      
        ############################################################
        sessions = Session.objects.all()
        week = Weekday.objects.order_by('-id').all()
        movies = Film.objects.order_by('-id').all()
        halls = Hall.objects.all()
        context = {

            'active_vkladka': active_vkladka,
            'sessions': sessions,
            'movies': movies,
            'halls': halls,
            'week': week,
        }
        return render(request, 'app_template/sessions.html', context)

class ReserveListView(View):
    
    
    def get(self, request, pk_hall, pk_movie, pk_session):
        hall = Hall.objects.get(id=pk_hall)
        movie = Film.objects.get(id=pk_movie)
        session = Session.objects.get(id=pk_session)

        places = Place.objects.filter(id_hall_id=pk_hall)
        tickets = Ticket.objects.all()
        
        

        context = {
            'hall': hall,
            'movie': movie,
            'session': session,
            'places': places,     
            'tickets': tickets,
            
        }
        return render(request, 'app_template/hall.html', context)
    
class ReservationView(View):
    

    def get(self, request, pk_movie, pk_session, number_hall, pk_place, pk_sector):

        

        movie = Film.objects.get(id=pk_movie)
        session = Session.objects.get(id=pk_session)
        time_sessions = Time_Sessions.objects.get(id = session.id_time_session_id)
        place = Place.objects.get(id=pk_place)
        sector = Sector.objects.get(id=pk_sector)
       
        num_hall = Hall.objects.get(number_hall = number_hall)
        
        type_time = time_sessions.time

        price_sess = session.price_session
        price_sect = sector.price_sector

        price_total = price_sess + price_sect

        context = {
            'movie': movie,
            'session': session,
            'place': place,
            'sector': sector,
            'num_hall': num_hall,
            'time_sessions': time_sessions,
            'price_total': price_total,
        }

        return render( request, 'app_template/reservations.html', context )

class ReserveDoneView(View):
    def get(self, request, pk_session, pk_place, total_sum):

        email = str(request.GET['email_input'])

        session      = Session.objects.get(id = pk_session)
        place        = Place.objects.get(id = pk_place)
        
        movie        = Film.objects.get(id = session.id_film_id)
        session_date = session.session_date
        time_sess    = Time_Sessions.objects.get(id = session.id_time_session_id)
        place_num    = place.place_number
        row_pl       = place.row_number
        hall_num     = Hall.objects.get(id = session.id_hall_id)
        sector       = Sector.objects.get( id = place.id_sector_id)
        
        # print(movie)
        # print(session_date)
        # print(time_sess)
        # print(hall_num)
        # print(place_num)
        # print(row_pl)
        # print(sector)
        # print(total_sum)

        messages = "Фільм: " +str(movie.name)+ "\nдата: " +str(session_date)+ "\nчас :" +str(time_sess.time)+ "\nзал №: " +str(hall_num.number_hall)+ "\nмісце: " +str(place_num)+ "\nряд: " +str(row_pl)+ "\nCектор: " +str(sector.name_sector)+ "\nЦіна: " +str(total_sum)+"\nчекаємо вас на сеанс!\n с повагою кінотеатр CINEMAX"
        # print(messages)
        send_mail('квиток на фільм',
            messages,
            'cinemacount12090@gmail.com',
            [email],
            fail_silently=False
        )

        Ticket(id_place_id = pk_place, id_session_id = pk_session, ticket_paid = total_sum).save()

        context = {

        }
    
        # return render(request, 'app_template/get_ticket.html')

        return HttpResponseRedirect(reverse('app:reserve', args = (hall_num.id, movie.id, pk_session) ))

class MovieListComments(View):
    
    def post(self, request, pk_movie, pk_user):


        
        if request.is_ajax():
            
            message = request.POST.get('comment') #

            Comments( comment = message, id_film_id = pk_movie, id_user_id = pk_user ).save()


            id_comment = Comments.objects.order_by('-id').filter(comment=message, id_user_id = pk_user)
            
            data = {
                'count_liked': id_comment[0].liked.all().count(),
                'count_dislike': id_comment[0].dislike.all().count(),

                'id_comment': int(id_comment[0].id),
                'comment': message,       
        }
    
            print('###'+message)
            return JsonResponse(data)

        # comm = request.POST['comment']
        # Comments(comment = comm, id_film_id = pk_movie, id_user_id = pk_user ).save()
        # print('fffff', form.fields['comment'])

        return HttpResponseRedirect(reverse("app:movie_detail", args = (pk_movie,) ))


class UpdateReview(View):
    def post(self, request):
        message_edited = request.POST.get('review_edited');
        id_review = request.POST.get('id_review');
        update_review = Comments.objects.get(id = id_review)
        update_review.comment = message_edited
        update_review.save()
        data = {
            'id_review': id_review,
            'review_edited': message_edited,
        }
        print(data)
        return JsonResponse(data)

class Delete_Review(View):
    def get(self, request):
        id_review = request.GET.get('id_review')
        Comments.objects.get(id = id_review).delete()

        data = {
            'deleted': True,
        }
        return JsonResponse(data)


class Liked_Review(View):
    def get(self, request):
        user = request.user
        review = Comments.objects.get(id = request.GET.get('id_review'))

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

        review = Comments.objects.get(id = request.GET.get('id_review'))
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