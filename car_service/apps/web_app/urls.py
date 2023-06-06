from django.urls import path, include
from .views import IndexView, ProfileView, GarageView, AddCar, CarEditView, error_page, ContactsView


urlpatterns = [
    path('', IndexView.as_view(), name='home page'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('garage/',include([
        path("", GarageView.as_view(), name='garage'),
        path("add/", AddCar.as_view(), name='customer add car page'),
        path("edit/<int:pk>", CarEditView.as_view(), name='car edit page')
        ])),
    
    path('error/', error_page),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
