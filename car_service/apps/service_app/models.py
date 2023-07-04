from django.db import models
from ..web_app.models import CustomerProfile
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmployeesProfile(models.Model):
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
        limit_choices_to={'is_customer': False},
    )
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class CarBrand(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    brand = models.CharField()
    image = models.CharField()
    
    
    def get_image(self):
        return self.image
    
    def __str__(self):
        return self.brand
    
    
class Cars(models.Model):
    
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    model = models.CharField()
    year = models.DateField()
    VIN = models.CharField()
    repair = models.BooleanField(
        default=False,
    )
    kilometers = models.CharField(
        null=True,
        blank=True,
    )
    
    registration_number = models.CharField(
        null=True,
        blank=True,
        unique=True
    )
    have_history= models.BooleanField(
        default=False,
    )
    
    user_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )
    
    def __str__(self):
        return f"{self.brand} - {self.registration_number}"

    
class RepairHistory(models.Model):
    def default_json():
        return  {
            "Date": "", 
            "Kilometers": "",
            "Changed parts": {
                
            }
        }
        
    car_id = models.ForeignKey(
        Cars,
        on_delete=models.CASCADE,        

    )
    history = models.JSONField(
        default=default_json
    )
    
    

class CarQueue(models.Model):
    TYPE_STATUS = (
        ('Awaiting To Take', 'Awaiting To Take'),
        ('Investigating Car', 'Investigating Car'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        
    )
    car_id = models.OneToOneField(
        Cars,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name="Customer Car",
        

    )
    
    mechanic_id = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Mechanic",
    )
    
    status = models.CharField(
        choices=TYPE_STATUS,
        max_length=20,
        null=True,
        blank=True,
    )
    
    
    def get_choices(self):
       return [choice[0] for choice in self.TYPE_STATUS]