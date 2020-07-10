from django.contrib import admin
from .models import Film, Hall, Time_Sessions, Session, Place, Ticket, Sector, Genre, Actor, Weekday, Comments, Name_Cinema
from modeltranslation.admin import TranslationAdmin


class FilmAdmin(TranslationAdmin):
    list_display = [ field.name for field in Film._meta.fields if field.name != "desc" and field.name != "desc_uk" and field.name != "desc_en"]
    search_fields = ['contry', 'year']
    list_filter = ['contry', 'year', 'created_at']
    class Meta:
        model = Film


class HallAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Hall._meta.fields]

    class Meta:
        model = Hall

class CommentsAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Comments._meta.fields]
    search_fields = ['id_user__username']
    list_filter = ['created_at']
    class Meta:
        model = Comments

class SessionAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Session._meta.fields]
    
    list_filter = ['id_hall__number_hall']
    class Meta:
        model = Session

class TicketAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Ticket._meta.fields]

    class Meta:
        model = Ticket


class SectorAdmin(TranslationAdmin):
    list_display = [ field.name for field in Sector._meta.fields]

    class Meta:
        model = Sector

class PlaceAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Place._meta.fields ]
    search_fields = ['row_number',]
    list_filter = ['id_hall__number_hall']
    class Meta:
        model = Place

class GenreAdmin(TranslationAdmin):
    list_display = [ field.name for field in Genre._meta.fields]
    search_fields = ['name',]
    
    class Meta:
        model = Genre

class ActorAdmin(TranslationAdmin):
    list_display = [ field.name for field in Actor._meta.fields if field.name != "biography" and field.name != "biography_uk" and field.name != "biography_en"]
    search_fields = ['name',]
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
admin.site.register(Weekday)
admin.site.register(Name_Cinema)

# admin.site.register(Weekday)


admin.site.register(Time_Sessions, Time_SessionsAdmin)
