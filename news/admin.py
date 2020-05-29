from django.contrib import admin

from .models import ParseMovieInfo, ArticleComment, LikePost

admin.site.register(ParseMovieInfo)
admin.site.register(LikePost)
admin.site.register(ArticleComment)
