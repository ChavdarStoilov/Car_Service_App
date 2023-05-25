from django.contrib.auth import get_user_model, forms as auth_forms
from ..service_app.models import PersonalProfile
from ..web_app.models import CustomerProfile
from django import forms

UserModel = get_user_model()


class CustomerUserCreation(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
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
      
      profile=CustomerProfile(
        first_name = first_name,
        last_name = last_name,
        user_id=user,
      )
      
      if commit:
        profile.save()
        
    
class PersonalUserCreation(auth_forms.UserCreationForm):
  
    class Meta:
      model = UserModel
      fields = (
      UserModel.USERNAME_FIELD,
      'password1',
      'password2',
    )
      
    def save(self, commit=True):
      
      user=super().save(commit=commit)
      
      profile=PersonalProfile(
        user_id=user,
      )
      
      if commit:
        profile.save()


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = (
          "username", "is_customer"
          )