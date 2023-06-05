from django import forms
from .models import CarQueue, Cars, CustomerProfile
from django.contrib.auth import get_user_model, forms as auth_forms

UserModel = get_user_model()

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
            'brand', 'model', 'year', 'VIN', 'registration_number', 'user_id'
        )
        
        
class AddCustomerFrom(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    
    class Meta:
      model = UserModel
      fields = [
      UserModel.USERNAME_FIELD,
      'password1',
      'password2',
      'first_name',
      'last_name',
    ]
    
    def save(self, commit=True):
      self.instance.is_customer = True
      user=super().save(commit=commit)
      first_name = self.cleaned_data['first_name']
      last_name = self.cleaned_data['last_name']
      email = self.cleaned_data['email']
      phone = self.cleaned_data['phone']
      
      
      profile=CustomerProfile(
        first_name = first_name,
        last_name = last_name,
        email = email,
        phone = phone,
        user_id=user,
      )
      
      if commit:
        profile.save()