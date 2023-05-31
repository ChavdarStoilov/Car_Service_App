from django.core.exceptions import ValidationError
from ..service_app.models import Cars


def validator_car_numbers(registration_number):
    exist = Cars.objects.filter(registration_number=registration_number)
    if exist:
        raise ValidationError(
            f'Car with the { registration_number } already exist'
            ) 