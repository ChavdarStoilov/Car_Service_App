from .models import CustomerProfile
from django import forms
from ..service_app.models import Cars, CarBrand
from .validators import validator_car_numbers, validator_car_kilometers, validator_car_vin


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
    BRAND = None
    
    CHOICES = [(brand.pk, brand.brand) for brand in CarBrand.objects.all()]
    
    brand = forms.ChoiceField( 
        choices=CHOICES, 
        required=False,
        widget=forms.Select(
            attrs={
                'class':'brands-choide'
            }
        )
    )
    
    
    model = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'field',
                'placeholder':"Example: A4"
            }
        )
    )

    year = forms.DateTimeField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'class':'field',
                'placeholder':"Example: 2000-01-01"
            }
        ),
    )
    
    kilometers = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'field',
                'placeholder':"Example: 100 000"
            }
        ),
        validators= [validator_car_kilometers],
    )
    
    VIN = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'field',
                'placeholder':"Example: WASDW20201WDA"
            }
        ),
        validators=[validator_car_vin],
    )

    registration_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'field',
                'placeholder':"Example: СА 1111 СА"
            }
        ),
        validators=[validator_car_numbers],
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
        self.BRAND = CarBrand.objects.get(pk = int(cleaned_data['brand']))
        cleaned_data['brand'] = self.BRAND

        
        # if self.__class__.__name__ == "AddCarFrom":
        #     car_number = cleaned_data.get('registration_number')
        #     validator_car_numbers(car_number)
        
        return cleaned_data
        
    def save(self, user_pk, commit=True):
        
        self.instance.user_id_id = int(user_pk)
        super().save(commit=commit)
        
