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
    liked = models.ManyToManyField(User, default = None, blank = True, related_name = 'liked')
    dislike = models.ManyToManyField(User, default = None, blank = True, related_name = 'dislike')
    url = models.SlugField(max_length = 300)
    
    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

    @property
    def num_dislikes(self):
        return self.dislike.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class LikePost(TimeStampMixin, models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_article = models.ForeignKey(ParseMovieInfo, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

    def __str__(self):
        return self.id_article.title
        
class DislikePost(TimeStampMixin, models.Model):
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_article = models.ForeignKey(ParseMovieInfo, on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length = 20)

    def __str__(self):
        return self.id_article.title

class ArticleComment(TimeStampMixin, models.Model):
    comment = models.TextField()
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_article = models.ForeignKey(ParseMovieInfo, on_delete = models.CASCADE)
    

    

    def __str__(self):
        return self.id_article.title ##########################