from django.contrib.auth import get_user_model, forms as auth_forms
from ..service_app.models import PersonalProfile
from ..web_app.models import CustomerProfile

UserModel = get_user_model()


class CustomerUserCreation(auth_forms.UserCreationForm):

    
    class Meta:
      model = UserModel
      fields = (
      UserModel.USERNAME_FIELD,
      'password1',
      'password2',
    )
    
    def save(self, commit=True):
      self.instance.is_customer = True
      user=super().save(commit=commit)
      
      profile=CustomerProfile(
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