from django.urls import path
from .views import IndexView, CarQueueVeiw, CarsVeiw, AddCarView, CustomersView, AddCustomerView


urlpatterns = [
    path('', IndexView.as_view(), name='service home page'),
    path('car-queue', CarQueueVeiw.as_view(), name='car queue'),
    path('cars', CarsVeiw.as_view(), name='cars'),
    path('add_car', AddCarView.as_view(), name='add car page'),
    path('customers', CustomersView.as_view(), name='customers page'),
    path('add_customers', AddCustomerView.as_view(), name='add customer page'),
]
