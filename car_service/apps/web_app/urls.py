from django.urls import path, include
from .views import IndexView, ProfileView, GarageView, AddCar, \
    ContactsView, CarRepairProcessView, CarHistoryView, \
    CarDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='home page'),
    path('profile/', include([
        path('', ProfileView.as_view(), name='profile'),
    ])),
    
    path('garage/',include([
        path("", GarageView.as_view(), name='garage'),
        path("add/", AddCar.as_view(), name='customer add car page'),
        path("process/<int:pk>", CarRepairProcessView.as_view(), name='car process page'),
        path("history/<int:pk>", CarHistoryView.as_view(), name='car history page'),
        path("delete/<int:pk>", CarDeleteView.as_view(), name='car delete page'),
        ])),

    path('contacts/', ContactsView.as_view(), name='contacts'),
]
