from django.urls import include, path
from .views import IndexView, CarQueueVeiw, CarsVeiw, AddCarView, \
    CustomersView, AddCustomerView, AddCarInQueueView, AddHisotryView, \
    ProfiileView


urlpatterns = [
    path('', IndexView.as_view(), name='service home page'),
    
    path('profile/<int:pk>', ProfiileView.as_view(), name='employee profile'),
    
    path('car-queue/', CarQueueVeiw.as_view(), name='car queue'),
    path('cars/', include([
        path('',CarsVeiw.as_view(), name='cars'),
        path("add-queue/<int:pk>", AddCarInQueueView.as_view(), name='add car in queue'),
        path("add-history/<int:pk>", AddHisotryView.as_view(), name='add car history'),
        
        ])),
    path('add_car/', AddCarView.as_view(), name='add car page'),
    path('customers/', CustomersView.as_view(), name='customers page'),
    path('add_customers/', AddCustomerView.as_view(), name='add customer page'),
]
