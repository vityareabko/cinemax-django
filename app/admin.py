from django.contrib import admin
from .models import Film, Hall, Time_Sessions, Session, Place, Ticket, Sector, Genre, Actor, Weekday, Comments



class FilmAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Film._meta.fields if field.name != "desc"]

    class Meta:
        model = Film


class HallAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Hall._meta.fields]

    class Meta:
        model = Hall

class CommentsAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Comments._meta.fields]

    class Meta:
        model = Comments

class SessionAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Session._meta.fields]

    class Meta:
        model = Session

class TicketAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Ticket._meta.fields]

    class Meta:
        model = Ticket


class SectorAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Sector._meta.fields]

    class Meta:
        model = Sector

class PlaceAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Place._meta.fields ]

    class Meta:
        model = Place

class GenreAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Genre._meta.fields]

    class Meta:
        model = Genre

class ActorAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Actor._meta.fields if field.name != "biography"]

    class Meta:
        model = Actor

class Time_SessionsAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Time_Sessions._meta.fields ]

    class Meta:
        model = Time_Sessions



admin.site.register(Film, FilmAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)

# admin.site.register(Weekday)


admin.site.register(Time_Sessions, Time_SessionsAdmin)
