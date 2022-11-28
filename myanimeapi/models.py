from django.db import models

# Create your models here.
class MyAnimeList(models.Model):
    Anime_id = models.AutoField(primary_key=True)
    Anime_Name = models.CharField(max_length=10000)