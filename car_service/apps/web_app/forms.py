from .models import CustomerProfile
from django import forms

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model= CustomerProfile
        fields =(
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
        )