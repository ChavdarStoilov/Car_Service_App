from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from .forms import ProfileForm, AddCarFrom, CarDetailsForm
from .models import CustomerProfile
from django.urls import reverse_lazy
from ..service_app.models import Cars, CarQueue, CarBrand, RepairHistory, PersonalProfile
from ..auth_app.models import AppUsers


class IndexView(TemplateView):
    template_name ='customer/new-home-page.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cars'] = CarBrand.objects.all()
        return context
    

class ProfileView(TemplateView):
    template_name ='customer/profile-details.html'
    
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
    
    
class CarEditView(TemplateView):
    template_name = 'customer/car-details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        car = Cars.objects.get(pk = kwargs['pk'])
        context['car'] = car
        context['form'] = CarDetailsForm(instance=car)
        return context


class CarRepairProcessView(TemplateView):
    template_name = 'customer/car-repair-process.html'
    
    def get(self, **kwargs):

        try:
            CarQueue.objects.get(pk = kwargs['pk'])
        except:
            return redirect('garage')
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            car = CarQueue.objects.get(pk = kwargs['pk'])
            context['car'] = car
            
        except:
            return redirect(reverse_lazy('garage'))
        
        return context
        

    
    
def error_page(request):
    return render(request, '404.html')


class ContactsView(IndexView, TemplateView):
    template_name ='customer/contacts.html'
    
    
class CarHistoryView(TemplateView):
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
        