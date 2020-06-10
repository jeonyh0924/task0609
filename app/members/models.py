from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    created = models.DateField(auto_now_add=True, )
