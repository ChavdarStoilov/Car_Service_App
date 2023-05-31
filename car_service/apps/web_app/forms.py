from typing import Any, Dict
from .models import CustomerProfile
from django import forms
from ..service_app.models import Cars, CarBrand
from .validators import validator_car_numbers
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field'}))
    last_name = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field'}))
    email = forms.EmailField(widget=forms.TextInput
        (attrs={'class':'field'}))
    phone = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field'}))
    
    
    class Meta:
        model= CustomerProfile
        fields =(
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
        )
        
        
class AddCarFrom(forms.ModelForm):
    
    CHOICES = [(brand.pk, brand.brand) for brand in CarBrand.objects.all()]
    
    brand = forms.ChoiceField( 
        choices=CHOICES, 
        required=False,
        widget=forms.Select(attrs={'class':'brands'})
    )
    
    
    model = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field',
            'placeholder':"Example: A4"}))
    year = forms.DateTimeField(widget=forms.DateInput
        (attrs={'class':'field',
            'placeholder':"Example: 2000-01-01"}))
    kilometers = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field',
            'placeholder':"Example: 100 000"}))
    VIN = forms.CharField(widget=forms.TextInput
        (attrs={'class':'field',
            'placeholder':"Example: WASDW20201WDA"}))
    registration_number = forms.CharField(
        widget=forms.TextInput(attrs={'class':'field',
            'placeholder':"Example: СА 1111 СА"}
        ),
        )
    
    class Meta:
        model = Cars
        fields = (
            'brand',
            'model',
            'year',
            'kilometers',
            'VIN',
            'registration_number'
        )
        
        
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['brand'] = CarBrand.objects.get(pk = int(cleaned_data['brand']))

        car_number = cleaned_data.get('registration_number')
        validator_car_numbers(car_number)
        
        return cleaned_data
        
    def save(self, user_pk, commit=True):
        
        self.instance.user_id_id = int(user_pk)
        super().save(commit=commit)