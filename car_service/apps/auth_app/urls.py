from django.urls import path
from django.contrib.auth import views
from .views import SingUpPersonalView, SingUpView, SingInView, logout_view


urlpatterns = [
    path('sing-up/', SingUpView.as_view(), name='singup page'),
    path('sing-in/', SingInView.as_view(), name='singin page'),
    path('logout/', logout_view, name='logout'),
    path('personal-sing-up/', SingUpPersonalView.as_view(), name='personal-sing-up'),
    
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
