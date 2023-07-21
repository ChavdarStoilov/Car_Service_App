from django.contrib.auth import get_user_model, forms as auth_forms, password_validation
from ..service_app.models import EmployeesProfile
from ..web_app.models import CustomerProfile
from django import forms
from django.utils.translation import gettext_lazy as _
from .validators import validator_username, validator_first_name, validator_last_name

UserModel = get_user_model()


class CustomerUserCreation(auth_forms.UserCreationForm):
    username = forms.CharField(
      validators=[validator_username]  
    )
    
    first_name = forms.CharField(
      validators=[validator_first_name]
    )
    last_name = forms.CharField(
      validators=[validator_last_name]
    )
    
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
        
      return user
        
    
class EmployeeUserCreation(auth_forms.UserCreationForm):
  
    class Meta:
      model = UserModel
      fields = (
      UserModel.USERNAME_FIELD,
      'password1',
      'password2',
    )
      
    def save(self, commit=True):
      
      user=super().save(commit=commit)
      
      profile=EmployeesProfile(
        user_id=user,
      )
      
      if commit:
        profile.save()

      return user

class UserChangeForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = (
          "username", "is_customer"
          )
        
        
        
class CustomPasswordChange(auth_forms.PasswordChangeForm):
  old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
              "autocomplete": "current-password", 
              "autofocus": True,
              'class': 'field',
              "placeholder": "Enter Old Password",
            }
        ),
    )
  
  
  new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
          attrs={
            "autocomplete": "new-password",
            "class": 'field',
            "placeholder": "Enter New Password",
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
  
  new_password2 = forms.CharField(
      label=_("New password confirmation"),
      strip=False,
      widget=forms.PasswordInput(
        attrs={
          "autocomplete": "new-password",
          "class": 'field',
          "placeholder": "Repeat New Password",
          }
      ),
  )