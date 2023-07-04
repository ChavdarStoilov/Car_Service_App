from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()
    
class CustomerProfile(models.Model):
    MAX_LENGTH_NAMES = 20
    MAX_PHONE_LENGTH = 14
    first_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_NAMES,
    )
    email = models.EmailField(
        
    )
    phone = models.CharField(
        max_length=MAX_PHONE_LENGTH,
    )
    
    user_id = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'