from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField
from accounts.models import User

"""
class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    categories_verified = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='')
    color_iqroom = models.CharField(
        max_length=6, choices=COLOR_CHOICES, default='green')

"""


class PostModel(models.Model):
    username = models.CharField(max_length=100)
    DateTimeField = models.DateTimeField(max_length=100)
    category_verified = models.Field()
    comment = models.CharField(max_length=10000)
