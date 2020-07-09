from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class custom_user(AbstractUser):
    '''  governrate = models.CharField(max_length=10, blank=True)
      city = models.CharField(max_length=10, blank=True)
      building = models.CharField(max_length=30, blank=True)
      street = models.CharField(max_length=100, blank=True)
      floor = models.IntegerField(blank=True)
      apartment = models.CharField(max_length=20, blank=True)'''
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
