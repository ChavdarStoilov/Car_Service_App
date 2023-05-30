from django.urls import path
from .views import IndexView, ProfileView, GarageView


urlpatterns = [
    path('', IndexView.as_view(), name='home page'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('garage', GarageView.as_view(), name='garage'),
    
]
