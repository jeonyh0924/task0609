from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    created = models.DateField(auto_now_add=True, )


class Card(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    no = models.IntegerField(default=0)
    
