from django.contrib import admin

from .models import ParseMovieInfo, ArticleComment

admin.site.register(ParseMovieInfo)
admin.site.register(ArticleComment)