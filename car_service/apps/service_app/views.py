from typing import Any, Dict
from django.db import models
from django.shortcuts import render, redirect
from .models import PersonalProfile, Cars, CarQueue
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AddCarFrom

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

        
    def post(self, request):
        if request.method == 'POST':
            car_pk = int(request.POST.get('submitter')[0])
            new_status = request.POST.get('submitter')[2:]
            if car_pk:
                car = CarQueue.objects.get(pk=car_pk)
                car.status=new_status
                car.save()
            return redirect(reverse_lazy('car queue'))
    
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
        context['my_total'] = AddCarFrom()
        return context
    
    def post(self, request):
        form = AddCarFrom(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect(reverse_lazy('cars'))