from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import AppUserManager

class AppUsers(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        default=True
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )
    is_customer = models.BooleanField(
        default=False,
    )
    
    
    
    USERNAME_FIELD = 'username'
    objects = AppUserManager()

    def __str__(self) -> str:
        return self.username