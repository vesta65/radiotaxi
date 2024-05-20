from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ci = models.CharField(max_length=20, unique=True, null=True, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True)
    numtelefonico = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
