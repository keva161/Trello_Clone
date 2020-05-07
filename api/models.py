from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Board(models.Model):
    board_owner = models.ForeignKey(User, related_name="created_boards", on_delete=models.CASCADE)
    board_name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.board_name

class List(models.Model):
    list = models.ForeignKey(Board, related_name="lists", on_delete=models.CASCADE)
    list_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.list_name

class Card(models.Model):
    card = models.ForeignKey(List, related_name="list_items", on_delete=models.CASCADE)
    card_name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.card_name