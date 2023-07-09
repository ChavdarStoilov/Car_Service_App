from django.shortcuts import render, redirect
from .models import Cars, CarQueue
from ..web_app.models import CustomerProfile
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import AddCarFrom, AddCustomerFrom, AddCarQueueFrom, AddHistoryForm
from datetime import date


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "service/index.html"
    login_url = reverse_lazy('singin page')
    permission_denied_message = "Do not have access for this url"
 
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_customer:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
        

class CarQueueVeiw(IndexView):
    template_name = "service/car_queue.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['queue'] = CarQueue.objects.all()
        
        return context

    def post(self, request):
        data = request.POST.get('submitter').split(",")
        car_pk = int(data[0])
        new_status = data[1]
        if car_pk:
            self.change_car_status(car_pk, new_status)
           
            if new_status == 'Done':
               self.change_repair_car_status(car_pk)
                           
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

        
    
class CarsVeiw(generic.ListView):
    template_name = "service/cars.html"
    model = Cars
    context_object_name = "cars"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['car_done'] = CarQueue.objects.filter(status="Done")
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(registration_number__icontains=search)
        return queryset


class AddCarView(generic.CreateView):
    template_name = "service/add-car.html"
    form_class = AddCarFrom
    success_url  = reverse_lazy('cars')
    
    
class CustomersView(generic.ListView):
    template_name = "service/customers.html"
    model = CustomerProfile
    context_object_name = "customers"
    

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
        context['car_pk'] = kwargs['pk']
        context['queue_from'] = AddCarQueueFrom(
            initial={
                'car_id': kwargs['pk'],
                'status': 'Awaiting To Take',
            }
        )
        return context
    
    def post(self, request, **kwargs):
        car_pk = kwargs["pk"]
        form = AddCarQueueFrom(
            request.POST, initial={
                'car_id': kwargs['pk'],
                'status': 'Awaiting To Take',
            }
        )
        if form.is_valid():
            form.save(car_pk)
            return redirect(reverse_lazy('cars'))
        
        
class AddHisotryView(IndexView):
    template_name = "service/car-history.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['car_pk'] = kwargs["pk"]
        return context

    def post(self, request, **kwargs):
        form = request.POST
        car_pk = kwargs["pk"]
        
        the_date = date.today()
        kilometers = form["kilometers"]
        
        parts = [row.split(" - ") for row in form["parts"].split(", ")]

        changed_parts = {
        }
        
        for part in parts:
            changed_parts[part[0]] = {
                "qty": int(part[1]),
                "price": int(part[2].replace(",", ""))
            }
        
        

        data = {
            "car_id": car_pk,
            "history":{
                "Date" : the_date.strftime("%d-%m-%Y"),
                "Kilometers": kilometers,
                "Changed parts": changed_parts
            }
        }
                
         
        form = AddHistoryForm(data)
        
        if form.is_valid():
            form.save()
            
            car = Cars.objects.get(pk=car_pk)
            car.have_history = True
            car.save()
            
            carqueue = CarQueue.objects.get(pk = car_pk)
            carqueue.delete()

        return redirect(reverse_lazy('cars'))


        