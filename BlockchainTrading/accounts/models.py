from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.

# to add new fields to existing User class:
# class AppUser(AbstractUser):
#     age = models.PositiveSmallIntegerField()

# to completely replace the User class:

# class AppUser(AbstractUser, PermissionsMixin):
#     USERNAME_FIELD = 'email'
#     pass
