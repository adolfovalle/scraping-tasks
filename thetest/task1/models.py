from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=200)
    user_id = models.IntegerField()
    n_followers = models.IntegerField()
    n_followees = models.IntegerField()

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mediaid = models.IntegerField()
    date_utc = models.DateTimeField()
    caption = models.TextField(blank=True, null=True)
    video_view_count = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField()
    comments = models.IntegerField()

# Create your models here.
