from django.shortcuts import render, redirect
from .models import PersonalProfile, Cars, CarQueue, CustomerProfile
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AddCarFrom, AddCustomerFrom, AddCarQueueFrom

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "service/index.html"
    login_url = reverse_lazy('singin page')
    permission_denied_message = "Do not have access for this url"
 
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_customer:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
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
        car_pk = int(request.POST.get('submitter')[0])
        new_status = request.POST.get('submitter')[2:]
        if car_pk:
            self.change_car_status(car_pk, new_status)
           
            if new_status == 'Done':
               self.change_repair_car_status(car_pk)
               
               #TODO: Write function for create car hisotry and remove from car queue
            
        return redirect(reverse_lazy('car queue'))
    
    
    def change_car_status(self, *args, **kwargs):
        pk = args[0]
        new_status = args[1]
        car = CarQueue.objects.get(pk=pk)
        car.status=new_status   
        car.save()
        
        
    def change_repair_car_status(self, *args, **kwargs):
        pk = args[0]
        car = Cars.objects.get(pk=pk)
        car.repair = False
        car.save()

        
    
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
        
        return redirect(reverse_lazy('car'))
    
    
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
        context['queue_from'] = AddCarQueueFrom()
        return context
    
    def post(self, request):
        form = AddCarQueueFrom(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('cars'))