from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField()
    is_tutor = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + self.last_name
