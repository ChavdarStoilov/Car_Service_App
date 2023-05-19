from django.urls import path
from .views import SingUpPersonalView, SingUpView, SingInView


urlpatterns = [
    path('sing-up/', SingUpView.as_view(), name='singup page'),
    path('sing-in/', SingInView.as_view(), name='singin page'),
    path('personal-sing-up/', SingUpPersonalView.as_view(), name='personal-sing-up'),
]
