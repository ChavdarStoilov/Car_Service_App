from django import forms
from .models import CarQueue, Cars, CustomerProfile, RepairHistory, PersonalProfile
from django.contrib.auth import get_user_model, forms as auth_forms

UserModel = get_user_model()
      
  
class AddCarQueueFrom(forms.ModelForm):     

    mechanics = [(person.pk, person) for person in PersonalProfile.objects.all() if person.position == "Mechanic"]
    
    mechanic_id = forms.ChoiceField( 
        choices=mechanics, 
        required=True,
      )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["car_id"].disabled = True
        self.fields["car_id"].widget.attrs["readonly"] = True
        self.fields["status"].disabled = True
        self.fields["status"].widget.attrs["readonly"] = True
        
    class Meta:
        model = CarQueue
        
        fields = (
          "car_id",
          "mechanic_id",
          "status",
        )
        
    def save(self, pk, commit=True):
      super().save(commit=commit)
      car = Cars.objects.get(pk = pk)
      car.repair  = True
      if commit:
        car.save()
        
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
        
        
class AddHistoryForm(forms.ModelForm):
  
  class Meta:
    model=RepairHistory
    fields = '__all__'