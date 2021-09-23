from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = (
    ('admin', 'admin'),
    ('chef', 'chef')
)


class User(AbstractUser):
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=150)
