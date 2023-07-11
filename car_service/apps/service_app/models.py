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
    MAX_LENGTH_BRAND = 25
    MAX_LENGTH_IMAGE = 50
    
    
    id = models.AutoField(
        primary_key=True
    )
    brand = models.CharField(
        max_length=MAX_LENGTH_BRAND,
    )
    image = models.CharField(
        max_length=MAX_LENGTH_IMAGE,
        
    )
    
    
    def get_image(self):
        return self.image
    
    def __str__(self):
        return self.brand
    
    
class ServiceGallery(models.Model):
    MAX_LENGTH_IMAGE = 50
    
    image = models.CharField(
        max_length=MAX_LENGTH_IMAGE,
    )
    
class Cars(models.Model):
    MAX_LENGTH_MODEL = 10
    MAX_LENGTH_VIN = 30
    MAX_LENGTH_KILOMETERS = 8
    MAX_LENGTH_REGISTER_NUMBER =12
    
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
    )
    year = models.DateField()
    VIN = models.CharField(
        max_length=MAX_LENGTH_VIN,
    )
    repair = models.BooleanField(
        default=False,
    )
    kilometers = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LENGTH_KILOMETERS,
    )
    
    registration_number = models.CharField(
        null=True,
        blank=True,
        unique=True,
        max_length=MAX_LENGTH_REGISTER_NUMBER,
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