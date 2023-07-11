from django.db import models
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import AppUserManager

class AppUsers(AbstractBaseUser, PermissionsMixin):
    MAX_LENGTH_USERNAME = 25
    username = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=MAX_LENGTH_USERNAME,
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
    
    is_customer = models.BooleanField(
        default=False,
    )
    
    last_login =models.DateTimeField(("last login"), blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,

    )
    
    USERNAME_FIELD = 'username'
    objects = AppUserManager()

    def __str__(self) -> str:
        return self.username