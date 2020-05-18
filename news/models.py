from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class ParseMovieInfo(TimeStampMixin, models.Model):
    title = models.CharField(max_length = 500)
    date = models.CharField(max_length = 50)
    describe = models.TextField()
    url = models.SlugField(max_length = 150)

    def __str__(self):
        return self.title