from django.db import models
from django.utils import timezone
# AutoField(): хранит целочисленное значение, которое автоматически инкрементируется, обычно применяется для первичных ключей
# CharField(max_length=N)
# IntegerField(): хранит значение типа Number
# BooleanField() хранит значение True или False (0 или 1)
# DateField() хранит дату
# TimeField() хранит время
# TextField()

class Genre(models.Model):
    name =models. CharField(max_length = 150)

class Actor(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'media/actors/')

class Film(models.Model): # Фильм 
    name = models.CharField(max_length = 150)
    duration_film = models.TimeField() # '14:30'
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    desc = models.TextField()
    year = models.DateField()
    contry = models.CharField(max_length = 150)
    director = models.CharField(max_length = 150)
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE)
    premiere = models.CharField(max_length = 150)
    budget = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'media/posters/')
    def __str__(self):
        return self.name

class Hall(models.Model): # зал
    number_hall = models.IntegerField()
    number_of_row = models.IntegerField()
    number_of_seats_in_a_row = models.IntegerField()
    spaciousness = models.IntegerField()

    def __str__(self):
        return str(self.number_hall)

class Session(models.Model): # сеанс  
    id_film = models.ForeignKey(Film, on_delete = models.CASCADE) 
    session_date = models.DateField()
    session_time_start = models.TimeField() # '14:30'
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)

    def __str__(self):
       return str(self.session_time_start)

class Sector(models.Model): # сектор
    name_sector = models.CharField(max_length = 150)
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)

    def __str__(self):
        return self.name_sector

        
class Price(models.Model): # цена
    id_sector_price = models.ForeignKey(Sector, on_delete = models.CASCADE)
    id_session = models.ForeignKey(Session, on_delete = models.CASCADE)
    price = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.price)

class Place(models.Model): # место 
    place_number = models.IntegerField()
    row_number = models.IntegerField()
    id_hall = models.ForeignKey(Hall, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.place_number)

class Ticket(models.Model): # билет 
    id_session = models.ForeignKey(Session, on_delete = models.CASCADE)
    id_place = models.ForeignKey(Place, on_delete = models.CASCADE)
    ticket_paid = models.BooleanField(default = False)
    date_created_ticket = models.DateTimeField(
                   null=True, blank=True,
                   verbose_name=u'Fecha de creación')
    reservation_ticket = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.date_created_ticket)
