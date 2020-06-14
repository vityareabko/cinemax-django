from modeltranslation.translator import register, TranslationOptions
from .models import Genre, Actor, Film, Sector, Weekday


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('biography','name', 'birthplace', 'citizenship', 'career',)

@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'contry',)

@register(Sector)
class SectorTranslationOptions(TranslationOptions):
    fields = ('name_sector',)

@register(Weekday)
class WeekdayTranslationOptions(TranslationOptions):
    fields = ('weekday',)

