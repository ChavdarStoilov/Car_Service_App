from django import forms
from .models import CarQueue, Cars


class CarQueueFrom(forms.ModelForm):
    
    class Meta:
        model = CarQueue
        
        fields = (
            '__all__'
        )
        
class AddCarFrom(forms.ModelForm):
    
    class Meta:
        model = Cars
        fields = (
            'model', 'year', 'VIN', 'registration_number', 'user_id'
        )