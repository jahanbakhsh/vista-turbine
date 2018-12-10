from django.db import models
from Apps.users.models import User
import os


class News(models.Model):
    NEWS_TYPE = [(1,'Main'),(2,'Competition')]
    title = models.CharField(max_length=200)
    large_img = models.ImageField(upload_to='news/img')
    small_img = models.ImageField(upload_to='news/img')
    source = models.CharField(max_length=100)
    content = models.TextField()
    type = models.IntegerField(choices=NEWS_TYPE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User,related_name="row_created_by")
    updated_by = models.ForeignKey(User,related_name="row_updated_by")

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hieght = models.FloatField()
    position = models.CharField(max_length=20)
    number = models.IntegerField()
    image = models.ImageField(upload_to='player/img')