from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# AutoField(): хранит целочисленное значение, которое автоматически инкрементируется, обычно применяется для первичных ключей
# CharField(max_length=N)
# IntegerField(): хранит значение типа Number
# BooleanField() хранит значение True или False (0 или 1)
# DateField() хранит дату
# TimeField() хранит время
# TextField()

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Genre( TimeStampMixin, models.Model):
    name =models. CharField(max_length = 150)

    def __str__(self):
        return self.name

class Actor(TimeStampMixin, models.Model ): # актеры и режисеры
    name = models.CharField(max_length = 150)
    age = models.PositiveSmallIntegerField("Возраст")
    birthplace = models.CharField(max_length = 300)
    citizenship = models.CharField(max_length = 150)
    career = models.CharField(max_length = 150)
    biography = models.TextField("Биография")
    image = models.ImageField(upload_to = 'actors/')


    def __str__(self):
        return self.name

class Film(TimeStampMixin, models.Model): # Фильм 
    name = models.CharField(max_length = 150)
    duration_film = models.TimeField() # '14:30'
    desc = models.TextField()
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    contry = models.CharField(max_length = 150)
    genre = models.ManyToManyField(Genre, verbose_name="жанры")
    actor = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    premiere = models.CharField(max_length = 150)
    budget = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'posters/')
    url_trailer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Hall(TimeStampMixin, models.Model): # зал
    number_hall = models.IntegerField()
    number_of_row = models.IntegerField()
    number_of_seats_in_a_row = models.IntegerField()
    spaciousness = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number_hall)

    def save(self, *args, **kwargs):
        self.spaciousness = self.number_of_row * self.number_of_seats_in_a_row
        super(Hall, self).save(*args, **kwargs)


        k = 1
        Place.objects.filter(id_hall_id = self.id).delete()
        sectors = Sector.objects.all()



        


        # for i in range(1, self.number_of_row+1):
        #     for j in range(1, self.number_of_seats_in_a_row+1):
        #         if k <= divmod(self.spaciousness, 3)[0]:
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 1).save()
                
        #         if k > divmod(self.spaciousness,3)[0] and k <= (divmod(self.spaciousness,3)[0]+divmod(self.spaciousness,3)[0]):
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 2).save()
                 
        #         if k > (divmod(self.spaciousness,3)[0]+divmod(self.spaciousness,3)[0]) and k <= self.spaciousness:
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 3).save()
        #         k+=1

        # for i in range(1, self.number_of_row+1):
        #     for j in range(1, self.number_of_seats_in_a_row+1):
        #         if k <= self.spaciousness // 3:
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 1).save()
                
        #         if k > self.spaciousness // 3 and k <= self.spaciousness // 1.5:
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 2).save()
                 
        #         if k > self.spaciousness // 1.5 and k <= self.spaciousness:
        #             Place(place_number = j, row_number = i, id_hall_id = self.id, id_sector_id = 3).save()
        #         k+=1
                    
       
        
        k = 1
        n = 0
        s = 1
        for i in sectors:
            
            for j in  range(k, (self.number_of_row // ((sectors.count()-n)) )+1):
                
                for z in range(1, self.number_of_seats_in_a_row+1):
                    Place(place_number = s, row_number = j, id_hall_id = self.id, id_sector_id = i.id).save()
                    s += 1
                k+=1
                # print(k)
                
                
            n += 1
    
            
                
                



class Time_Sessions(TimeStampMixin, models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class Session(TimeStampMixin, models.Model): # сеанс  
    id_film = models.ForeignKey(Film, on_delete = models.CASCADE) 
    session_date = models.DateField()
    id_time_session = models.ForeignKey(Time_Sessions, on_delete = models.CASCADE)
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
    price_session = models.PositiveIntegerField()

    def __str__(self):
       return str("Дата: " + str(self.session_date) + ' время: '+ str(self.id_time_session) +' зал: ' + str(self.id_hall))

class Sector(TimeStampMixin,models.Model): # сектор
    name_sector = models.CharField(max_length = 150)
    id_hall = models.ManyToManyField(Hall)
    price_sector = models.PositiveIntegerField()
    def __str__(self):
        return self.name_sector

        


class Place(TimeStampMixin, models.Model): # место 
    place_number = models.IntegerField()
    row_number = models.IntegerField()
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
    id_sector = models.ForeignKey(Sector, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id_hall)

class Ticket(TimeStampMixin, models.Model): # билет 
    id_session = models.ForeignKey(Session, on_delete = models.CASCADE)
    id_place = models.ForeignKey(Place, on_delete = models.CASCADE)
    ticket_paid = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id_session)

####################################################################

class Weekday(TimeStampMixin, models.Model):
    weekday = models.CharField(max_length=150)
    date = models.DateField()
    weekday_en = models.CharField(max_length=50)

    def __str__(self):
        return self.weekday

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Comments(TimeStampMixin, models.Model):
    comment = models.TextField()
    id_film = models.ForeignKey(Film, on_delete = models.CASCADE)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete = models.CASCADE, blank=True, null=True
    )
    
    liked = models.ManyToManyField(User, default = None, blank = True, related_name = 'liked_movie_review')
    dislike = models.ManyToManyField(User, default = None, blank = True, related_name = 'dislike_movie_review')

    @property
    def num_likes_review(self):
        return self.liked.all().count()

    @property
    def num_dislikes_review(self):
        return self.dislike.all().count()

    def __str__(self):
        return self.comment

class LikeReviewMovie(TimeStampMixin, models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_review = models.ForeignKey(Comments, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

    def __str__(self):
        return str(self.id_review)
        
class DislikeReviewMovie(TimeStampMixin, models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_review = models.ForeignKey(Comments, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

    def __str__(self):
        return str(self.id_review)


# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.db import models

# def created_hall(sender, instance, created, **kwargs):
#     if created:
#         Hall.objects.create(user = instance)
#         print("createв hall")

# post_save.connect(created_hall, sender=User)