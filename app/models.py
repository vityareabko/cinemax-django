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
    spaciousness = models.IntegerField()

    def __str__(self):
        return str(self.number_hall)

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
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
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

# LIKE_CHOICES = (
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike'),
# )
class Comments(TimeStampMixin, models.Model):
    comment = models.TextField()
    id_film = models.ForeignKey(Film, on_delete = models.CASCADE)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)

    # liked = models.ManyToManyField(User, default = None, blank = True, related_name = 'liked_movie_review')
    # dislike = models.ManyToManyField(User, default = None, blank = True, related_name = 'dislike_movie_review')

    # @property
    # def num_likes_review(self):
    #     return self.liked.all().count()

    # @property
    # def num_dislikes_review(self):
    #     return self.dislike.all().count()

    def __str__(self):
        return self.comment

# class LikeReviewMovie(TimeStampMixin, models.Model):
#     id_user = models.ForeignKey(User, on_delete = models.CASCADE)
#     id_review = models.ForeignKey(Comments, on_delete = models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

#     def __str__(self):
#         return str(self.id_review)
        
# class DislikeReviewMovie(TimeStampMixin, models.Model):
#     id_user = models.ForeignKey(User, on_delete = models.CASCADE)
#     id_review = models.ForeignKey(Comments, on_delete = models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

#     def __str__(self):
#         return str(self.id_review)