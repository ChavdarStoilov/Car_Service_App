from django.shortcuts import render, redirect
from .forms import CustomerUserCreation, PersonalUserCreation
from django.contrib.auth import views as auth_views, mixins as auth_mixins
from django.views import generic as views
from django.urls import reverse_lazy

class SingUpView(views.CreateView):
    template_name ='auth/singup.html'
    form_class = CustomerUserCreation

    # success_url = reverse_lazy('singin page')
    def get_success_url(self):

        return str(reverse_lazy('singin page')) 
    
class SingUpPersonalView(views.CreateView):
    template_name ='auth/singup.html'
    form_class = PersonalUserCreation

    # success_url = reverse_lazy('singin page')

    def get_success_url(self):

        return str(reverse_lazy('singin page')) 
    
    
class SingInView(auth_views.LoginView):
    template_name ='auth/singin.html'
    success_url = ""
    
    
    
    def get_success_url(self):
        if not self.request.user.is_customer:
            SingInView.success_url = reverse_lazy('service home page')
        else:
            SingInView.success_url = reverse_lazy('home page')
            
        if self.success_url:
            return self.success_url
        
        return self.get_success_url() or self.get_default_redirect_url()