from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=255,null=True)
    genre=models.CharField(max_length=255,null=True)
    director=models.CharField(max_length=255,null=True)
    
    