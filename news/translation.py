from modeltranslation.translator import register, TranslationOptions
from .models import ParseMovieInfo

@register(ParseMovieInfo)
class ParseMovieInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'short_describe', 'full_describe',)
