from django.core.exceptions import ValidationError
from ..service_app.models import Cars
from datetime import datetime

def validator_car_numbers(registration_number):
    exist = Cars.objects.filter(registration_number=registration_number)
    if exist:
        raise ValidationError(
            f'Car with the registration number { registration_number } already exist'
        )
    
    try:
        test_number = registration_number.split()
        if len(test_number[0]) < 1 or len(test_number[1]) < 4 or len(test_number[2]) < 1:
            raise ValidationError(
                    f'Car with the registration number { registration_number } already exist'
                )
    except:
        raise ValidationError(
            f'The registration number { registration_number } is not a valid!'
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
        