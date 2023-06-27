from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import ProfileForm, AddCarFrom
from .models import CustomerProfile
from django.urls import reverse_lazy
from ..service_app.models import Cars, CarQueue, CarBrand, RepairHistory, PersonalProfile
from ..auth_app.models import AppUsers
from rest_framework.response import Response


class IndexView(ListView):
    template_name ='customer/new-home-page.html'
    model = CarBrand
    context_object_name = "cars"

  
class ContactsView(IndexView):
    template_name ='customer/contacts.html'
      

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name ='customer/profile-details.html'
    login_url = reverse_lazy('singin page')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if not self.request.user.is_customer:
            user = PersonalProfile.objects.get(user_id_id  = self.request.user.pk)

        else:   
            user = CustomerProfile.objects.get(user_id_id  = self.request.user.pk)

        context['form_profile'] = ProfileForm(instance=user)
        return context

    def post(self, request):

        user = CustomerProfile.objects.get(user_id  = self.request.user)
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        


class GarageView(LoginRequiredMixin, ListView):
    template_name ='customer/garage.html'
    login_url = reverse_lazy('singin page')
    model = Cars
    context_object_name = "cars"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cars'] = Cars.objects.filter(user_id = self.request.user.pk)
        return context
    
    
class AddCar(LoginRequiredMixin, CreateView):
    template_name = 'customer/garage-add-car.html'
    form_class = AddCarFrom
    success_url = reverse_lazy('garage')
    context_object_name = "form"
    
    
    def post(self, request):
        car_form = AddCarFrom(request.POST)
        user_pk = request.user.pk
        if car_form.is_valid():
            car_form.save(user_pk)
            return redirect(reverse_lazy('garage'))
        else:
            return render(request, self.template_name, {'form': car_form })
    


class CarRepairProcessView(LoginRequiredMixin, DetailView):
    template_name = 'customer/car-repair-process.html'
    model = CarQueue
    context_object_name = "car"
    

    # def get(self, request, pk, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     car = self.get_object(pk)
    #     if not car:
    #         return redirect(reverse_lazy('garage'))
    #     context['car'] = self.get_object(pk)
    #     return self.render_to_response(context)

    
    
def error_page(request):
    return render(request, '404.html')

    
class CarHistoryView(LoginRequiredMixin, DetailView):
    template_name = 'customer/car-history.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cars_history = RepairHistory.objects.filter(car_id = kwargs['pk'])
        
        date_invoice_number = []
        
        for row in cars_history:
            car_history_datails = row.history
            total_price = [item["qty"] * item["price"] for item in car_history_datails['Changed parts'].values()]
            date_invoice_number.append(
                {
                    'date': car_history_datails['Date'],
                    'number':row.pk,
                    'total_price': sum(total_price),
                    'kilometers': car_history_datails["Kilometers"]
                }
            ) 

        context['history'] = date_invoice_number
        return context
        