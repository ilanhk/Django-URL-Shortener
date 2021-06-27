from django.db import models

# Create your models here.

class ShortURL(models.Model):
    original_url = models.URLField(max_length=800)
    short_url = models.CharField(max_length=200)
    time_date_created = models.DateTimeField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.original_url
