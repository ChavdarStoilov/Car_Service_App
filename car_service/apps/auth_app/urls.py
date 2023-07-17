from django.urls import path
from django.contrib.auth import views
from .views import SingUpView, SingInView, logout_view, CustomPasswordChangeView


urlpatterns = [
    path('sing-up/', SingUpView.as_view(), name='singup page'),
    path('sing-in/', SingInView.as_view(), name='singin page'),
    path('logout/', logout_view, name='logout'),

    path('password_change/', CustomPasswordChangeView.as_view(), name='change password page'),
]
