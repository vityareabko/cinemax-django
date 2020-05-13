from django.contrib import admin
from .models import Film, Hall, Time_Sessions, Session, Place, Ticket, Sector, Genre, Actor, Weekday

admin.site.register(Film)
admin.site.register(Hall)
admin.site.register(Time_Sessions)
admin.site.register(Session)
admin.site.register(Place)
admin.site.register(Ticket)
admin.site.register(Sector)
admin.site.register(Genre)
admin.site.register(Actor)

admin.site.register(Weekday)