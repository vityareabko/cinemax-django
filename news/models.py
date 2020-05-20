from django.db import models
from django.contrib.auth.models import User

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class ParseMovieInfo(TimeStampMixin, models.Model):
    title = models.CharField(max_length = 300)
    date = models.CharField(max_length = 50)
    short_describe = models.TextField()
    full_describe = models.TextField()
    
    url = models.SlugField(max_length = 300)
    
    def __str__(self):
        return self.title

class ArticleComment(TimeStampMixin, models.Model):
    comment = models.TextField()
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_article = models.ForeignKey(ParseMovieInfo, on_delete = models.CASCADE)
    id_parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )

    

    def __str__(self):
        return self.id_article.title ##########################