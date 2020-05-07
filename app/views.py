from django.shortcuts import render
from django.views.generic.base import View
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Film, Actor, Session, Time_Sessions, Hall, Place, Sector, Ticket

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
        return render(request, 'app_template/movie_detail.html', {'movie': movie})

class ActorDetailView(View):

    def get(self, request, pk):
        actor = Actor.objects.get(id=pk) 
        context = {
            'actor': actor,
        }
        return render(request, 'app_template/actor_detail.html', context)





class SessionsListView(View):
    
    def get(self, request):

        

        # for i in range(num_week_day, num_week_day + 6):
        #     if i == 0:
        #         pn = tday + datetime.timedelta(days=i)
        #         vt = tday + datetime.timedelta(days=1) #2
        #         sr = tday + datetime.timedelta(days=2) #3
        #         ct = tday + datetime.timedelta(days=3) #4
        #         pt = tday + datetime.timedelta(days=4) #5
        #         sb = tday + datetime.timedelta(days=5) #6
        #         nd = tday + datetime.timedelta(days=6) #7
        


        tday = date.today()
        num_week_day = date.today().weekday()
        
        # for i in range(0,6):
        #     pn = tday + datetime.timedelta(days=num_week_day-num_week_day) 
        #     vt = tday + datetime.timedelta(days=num_week_day+1)
        #     sr = tday + datetime.timedelta(days=num_week_day+2)
        #     ct = tday + datetime.timedelta(days=num_week_day+3)
        #     pt = tday + datetime.timedelta(days=num_week_day+4)
        #     sb = tday + datetime.timedelta(days=num_week_day+5)
        #     nd = tday + datetime.timedelta(days=num_week_day+6)

        if num_week_day == 0:
            pn = tday + datetime.timedelta(days=0) 
            vt = tday + datetime.timedelta(days=1)
            sr = tday + datetime.timedelta(days=2)
            ct = tday + datetime.timedelta(days=3)
            pt = tday + datetime.timedelta(days=4)
            sb = tday + datetime.timedelta(days=5)
            nd = tday + datetime.timedelta(days=6)
        if num_week_day == 1:
            pn = tday + datetime.timedelta(days=6) 
            vt = tday + datetime.timedelta(days=0)
            sr = tday + datetime.timedelta(days=1)
            ct = tday + datetime.timedelta(days=2)
            pt = tday + datetime.timedelta(days=3)
            sb = tday + datetime.timedelta(days=4)
            nd = tday + datetime.timedelta(days=5)
        if num_week_day == 2:
            pn = tday + datetime.timedelta(days=5) 
            vt = tday + datetime.timedelta(days=6)
            sr = tday + datetime.timedelta(days=0)
            ct = tday + datetime.timedelta(days=1)
            pt = tday + datetime.timedelta(days=2)
            sb = tday + datetime.timedelta(days=3)
            nd = tday + datetime.timedelta(days=4)
        if num_week_day == 3:
            pn = tday + datetime.timedelta(days=4) 
            vt = tday + datetime.timedelta(days=5)
            sr = tday + datetime.timedelta(days=6)
            ct = tday + datetime.timedelta(days=0)
            pt = tday + datetime.timedelta(days=1)
            sb = tday + datetime.timedelta(days=2)
            nd = tday + datetime.timedelta(days=3)
        if num_week_day == 4:
            pn = tday + datetime.timedelta(days=3) 
            vt = tday + datetime.timedelta(days=4)
            sr = tday + datetime.timedelta(days=5)
            ct = tday + datetime.timedelta(days=6)
            pt = tday + datetime.timedelta(days=0)
            sb = tday + datetime.timedelta(days=1)
            nd = tday + datetime.timedelta(days=2)
        if num_week_day == 5:
            pn = tday + datetime.timedelta(days=2) 
            vt = tday + datetime.timedelta(days=3)
            sr = tday + datetime.timedelta(days=4)
            ct = tday + datetime.timedelta(days=5)
            pt = tday + datetime.timedelta(days=6)
            sb = tday + datetime.timedelta(days=0)
            nd = tday + datetime.timedelta(days=1)
        
        if num_week_day == 6:
            pn = tday + datetime.timedelta(days=1) 
            vt = tday + datetime.timedelta(days=2)
            sr = tday + datetime.timedelta(days=3)
            ct = tday + datetime.timedelta(days=4)
            pt = tday + datetime.timedelta(days=5)
            sb = tday + datetime.timedelta(days=6)
            nd = tday + datetime.timedelta(days=0)
        
      
        

        # sessions_td = Session.objects.filter( session_date = today ).all()
        sessions_pn = Session.objects.filter(session_date = pn ).all()
        sessions_vt = Session.objects.filter(session_date = vt ).all()
        sessions_sr = Session.objects.filter(session_date = sr ).all()
        sessions_ct = Session.objects.filter(session_date = ct ).all()
        sessions_pt = Session.objects.filter(session_date = pt ).all()
        sessions_sb = Session.objects.filter(session_date = sb ).all()
        sessions_nd = Session.objects.filter(session_date = nd ).all()

        sessions_time = Time_Sessions.objects.all()
       

        
        movies = Film.objects.order_by('-id').all()
        halls = Hall.objects.all()
        context = {
            
            'sessions_pn': sessions_pn,
            'sessions_vt': sessions_vt,
            'sessions_sr': sessions_sr,
            'sessions_ct': sessions_ct,
            'sessions_pt': sessions_pt,
            'sessions_sb': sessions_sb,
            'sessions_nd': sessions_nd,
            'sessions_time': sessions_time,
            # 'sessions_time_pn': sessions_time_pn,
            # 'sessions_time_vt': sessions_time_vt,
            # 'sessions_time_sr': sessions_time_sr,
            # 'sessions_time_ct': sessions_time_ct,
            # 'sessions_time_pt': sessions_time_pt,
            # 'sessions_time_sb': sessions_time_sb,
            # 'sessions_time_nd': sessions_time_nd,     

            'movies': movies,
            'halls': halls
        }
        return render(request, 'app_template/sessions.html', context)

class ReserveListView(View):
    
    
    def get(self, request, pk_hall, pk_movie, pk_session):
        hall = Hall.objects.get(id=pk_hall)
        movie = Film.objects.get(id=pk_movie)
        session = Session.objects.get(id=pk_session)

        places = Place.objects.filter(id_hall_id=pk_hall)
        context = {
            'hall': hall,
            'movie': movie,
            'session': session,
            'places': places,     
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

        Ticket(id_place_id = pk_place, id_session_id = pk_session, ticket_paid = total_sum).save()

        context = {

        }
        
        return render(request, 'app_template/get_ticket.html')

# return HttpResponseRedirect(reverse('app:reserve', args = (pk_hall,pk_movie, pk_session) ))

# >>> tod_dict = {                                             
# ...
# ...
# ...
# ...             9: 'утро', 10: 'утро', 11: 'утро',
# ...             12: 'обед', 13: 'обед', 14: 'обед',
# ...             15: 'обеда', 16: 'обеда', 17: 'обеда',
# ...             18: 'вечер', 19: 'вечер', 20: 'вечер',
# ...             21: 'вечер', 22: 'вечер', 23: 'вечер'
# ...         }
# >>> tod_dict[a.hour] 