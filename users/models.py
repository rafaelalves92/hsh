from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
        "unique": "This field must be unique."
    })
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
