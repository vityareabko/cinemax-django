from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ParseMovieInfo, ArticleComment, LikePost


class ParseMovieInfoAdmin(TranslationAdmin):
    list_display = [ field.name for field in ParseMovieInfo._meta.fields if field.name != "full_describe_uk" and field.name != "short_describe_uk" and field.name != "full_describe_en" and field.name != "short_describe_en"]
    search_fields = ['title',]
    list_filter = ['created_at',]
    class Meta:
        model = ParseMovieInfo


admin.site.register(ParseMovieInfo, ParseMovieInfoAdmin)
admin.site.register(ArticleComment)
