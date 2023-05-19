from django.urls import path
from .views import IndexView, CarQueueVeiw, CarsVeiw


urlpatterns = [
    path('', IndexView.as_view(), name='home_page'),
    path('car-queue', CarQueueVeiw.as_view(), name='car queue'),
    path('cars', CarsVeiw.as_view(), name='cars'),
    
]
