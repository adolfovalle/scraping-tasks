from django.db import models

class VideoArticle(models.Model):
    url = models.CharField(max_length=300, unique=True)
    fecha = models.CharField(max_length=300)
    titulo = models.CharField(max_length=300)
    texto = models.TextField()
