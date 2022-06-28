from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#--------------------mtm relation------------------------
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=50)
    song_duration = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Song'

    def __str__(self):
        return self.song_name


#---------------------oto realtion-----------------------

class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default=2)
    page_name = models.CharField(max_length=50)
    page_cat = models.CharField(max_length=50)
    page_publish_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Page'
        
    def __str__(self):
        return self.page_name