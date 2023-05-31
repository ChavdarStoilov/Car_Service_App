from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from .forms import ProfileForm, AddCarFrom
from . models import CustomerProfile
from django.urls import reverse_lazy
from ..service_app.models import Cars

class IndexView(TemplateView):
    template_name ='customer/index.html'


class ProfileView(TemplateView):
    template_name ='customer/profile-details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = CustomerProfile.objects.get(user_id = self.request.user.pk)
        context['form_profile'] = ProfileForm(instance=user)
        return context

    def post(self, request):
        user = CustomerProfile.objects.get(user_id = self.request.user.pk)
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        


class GarageView(TemplateView):
    template_name ='customer/garage.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cars'] = Cars.objects.filter(user_id = self.request.user.pk)
        return context
    
    
class AddCar(TemplateView):
    template_name = 'customer/garage-add-car.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = AddCarFrom()
        return context
    
    
    def post(self, request):
        car_form = AddCarFrom(request.POST)
        user_pk = request.user.pk
        if car_form.is_valid():
            car_form.save(user_pk)
            return redirect(reverse_lazy('garage'))
        else:
            return render(request, self.template_name, {'form': car_form })
    