from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)

class Review(models.Model):
    text = models.TextField()  # Assuming you have a 'text' field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    watchAgain = models.BooleanField(default=False)

    def __str__(self):
        return self.text