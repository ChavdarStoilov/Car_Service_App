from django.shortcuts import render, redirect
from .models import PersonalProfile, Cars, CarQueue, CustomerProfile
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AddCarFrom, AddCustomerFrom, CarQueueFrom

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "service/index.html"
    login_url = reverse_lazy('singin page')
    redirect_field_name = reverse_lazy('home page')
 
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = PersonalProfile.objects.get(user_id=self.request.user.pk)
        
        return context
    

class CarQueueVeiw(IndexView):
    template_name = "service/car_queue.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['queue'] = CarQueue.objects.all()
        
        return context

        
    
class CarsVeiw(IndexView):
    template_name = "service/cars.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cars'] = Cars.objects.all()
        
        return context


class AddCarView(IndexView):
    template_name = "service/add-car.html"
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['car_from'] = AddCarFrom()
        return context
    
    def post(self, request):
        form = AddCarFrom(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect(reverse_lazy('cars'))
    
    
class CustomersView(IndexView):
    template_name = "service/customers.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['customers'] = CustomerProfile.objects.all()
        
        return context
    

class AddCustomerView(IndexView):
    template_name = 'service/add-customer.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer_form"] = AddCustomerFrom()
        return context
    
    def post(self, request):
        form = AddCustomerFrom(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect(reverse_lazy('customers page'))

class AddCarInQueueView(IndexView):
    template_name = 'service/add-car-queue.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['queue_from'] = CarQueueFrom()
        return context
    
    def post(self, request):
        form = CarQueueFrom(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('cars'))