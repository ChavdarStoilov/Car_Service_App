from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from .models import PersonalProfile, Cars, CarQueue
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from .forms import CarQueueFrom

class IndexView(LoginRequiredMixin, DetailView, TemplateView):
    template_name = "service/index.html"
    login_url = reverse_lazy('singin page')
    redirect_field_name = reverse_lazy('home page')
    

    def get(self, request):
        user = PersonalProfile.objects.get(pk=request.user.pk)
        cars = Cars.objects.all()
        car_queue = CarQueue.objects.all()
        context = {
            'user': user,
            'cars': cars,
            'queue': car_queue,
        }
        return self.render_to_response(context)

class CarQueueVeiw(IndexView):
    template_name = "service/car_queue.html"
    
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

