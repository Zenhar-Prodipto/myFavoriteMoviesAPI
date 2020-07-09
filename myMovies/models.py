from django.db import models

# Create your models here.
class Movie(models.Model):

    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False)
    imdb_rating = models.DecimalField(max_digits=3,decimal_places=2)
    timestamp_of_imdb = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name