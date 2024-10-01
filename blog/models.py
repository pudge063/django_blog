from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
