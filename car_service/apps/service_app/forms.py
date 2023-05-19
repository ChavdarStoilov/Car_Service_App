from django import forms
from .models import CarQueue


class CarQueueFrom(forms.ModelForm):
    
    class Meta:
        model = CarQueue
        
        fields = (
            '__all__'
        )