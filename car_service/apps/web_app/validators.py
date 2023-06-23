from django.core.exceptions import ValidationError
from ..service_app.models import Cars
from datetime import datetime

def validator_car_numbers(registration_number):
    exist = Cars.objects.filter(registration_number=registration_number)
    if exist:
        raise ValidationError(
            f'Car with the registration number { registration_number } already exist'
        ) 
        


def validator_car_kilometers(kilometers):
    int_kilometers = int(kilometers.replace(" ", ""))
    
    if int_kilometers < 0:
        raise ValidationError(
            'The kilometers cannot be negative'
        ) 



def validator_car_vin(vin):
    exist = Cars.objects.filter(VIN=vin)
    if exist:
        raise ValidationError(
            f'Car with VIN: { vin } already exist'
        ) 
        