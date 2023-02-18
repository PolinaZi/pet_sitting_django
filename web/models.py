from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Locality(models.Model):
    name = models.CharField(max_length=256)


class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=150)
    post_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opened = models.BooleanField(default=True)
    price = models.IntegerField()
    pets = models.ManyToManyField(Pet)
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL)
