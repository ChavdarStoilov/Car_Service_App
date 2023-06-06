from django.db import models
from ..auth_app.models import AppUsers
from ..web_app.models import CustomerProfile

class PersonalProfile(models.Model):
    MAX_LENGTH_NAMES = 20
    MAX_PHONE_LENGTH = 14
    
    POSTIONS = (
        ('Mechanic', 'Mechanic'),
        ('Reciver', 'Reciver'),
    )
    
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
    
    position = models.CharField(
        choices=POSTIONS,
        max_length=10,
        null=True,
        blank=True,
    )
    user_id = models.OneToOneField(
        AppUsers,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    
    
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
    
    
class TestCarsBrands(models.Model):
    brand = models.CharField()
    model = models.CharField(
        
    )
    # variants = models.CharField()
    
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
    history_id = models.OneToOneField(
        to='RepairHistory',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    user_id = models.ForeignKey(
        CustomerProfile,
        on_delete=models.CASCADE,

    )

    
class RepairHistory(models.Model):
    def default_json():
        return  {
            "date": "",
            "parts": {
                "part_name": "",
                "price": "",
            },
            "mechanic": "",
        }
        
    car_id = models.OneToOneField(
        Cars,
        primary_key=True,
        on_delete=models.CASCADE,        

    )
    hisory = models.JSONField(
        default=default_json
    )
    
    

class CarQueue(models.Model):
    TYPE_STATUS = (
        ('Awaiting To Take', 'Awaiting To Take'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        
    )
    car_id = models.OneToOneField(
        Cars,
        primary_key=True,
        on_delete=models.CASCADE,

    )
    
    mechanic_id = models.OneToOneField(
        PersonalProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    status = models.CharField(
        choices=TYPE_STATUS,
        max_length=16,
        null=True,
        blank=True,
    )
    
    
    def get_choices(self):
       return [choice[0] for choice in self.TYPE_STATUS]