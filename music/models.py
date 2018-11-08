from django.db import models

# Create your models here , schema for the music database.

class Album(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    image = models.CharField(max_length = 1000)
    nos = models.IntegerField()

class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    time = models.IntegerField()



