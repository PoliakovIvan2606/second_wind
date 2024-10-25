from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    ogrn = models.ManyToManyField('organization.Organization', blank=True, related_name='users_ogrn')

    def __str__(self):
        return self.username
