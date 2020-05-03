from django.utils import timezone
from django.db import models


# Create your models here.


class User(models.Model):

    username = models.CharField( max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username


class Kanban(models.Model):
    title = models.CharField(max_length=160, blank=True, unique=True)
    user = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now_add=True)
    lastupdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

