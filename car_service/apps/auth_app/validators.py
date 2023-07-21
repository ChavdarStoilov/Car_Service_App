from django.core.exceptions import ValidationError


def validator_username(username):
    
    if len(username) < 2:
        raise ValidationError(
            'The username must be at least 2 characters'
        ) 

def validator_first_name(name):
    
    if len(name) < 2:
        raise ValidationError(
            'The First Name must be at least 2 characters'
        ) 
        
def validator_last_name(name):
    
    if len(name) < 2:
        raise ValidationError(
            'The Last name must be at least 2 characters'
        )