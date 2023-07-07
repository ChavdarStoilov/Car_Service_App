from django.shortcuts import render, redirect
from .forms import CustomerUserCreation, CustomPasswordChange
from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home page')

class SingUpView(views.CreateView):
    template_name ='auth/singup.html'
    form_class = CustomerUserCreation
    success_url = reverse_lazy('singin page')
    
class SingInView(auth_views.LoginView):
    template_name ='auth/singin.html'    
    
    def get_success_url(self):
        if not self.request.user.is_customer and not self.request.user.is_staff and not self.request.user.is_superuser:
            return reverse_lazy('service home page')
        else:
            return reverse_lazy('home page')
            
    
class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'web/change_password.html'
    form_class = CustomPasswordChange
    success_url = reverse_lazy('change password page')