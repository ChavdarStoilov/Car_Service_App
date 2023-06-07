from django.urls import path, include
from rest_framework import routers
from .views import CarApiVeiw

router = routers.DefaultRouter()


urlpatterns = [
    path('', include([
        path('api-auth/', include('rest_framework.urls')),
        path('car/', include([
            path('', CarApiVeiw.as_view()),
            path('<int:pk>/', CarApiVeiw.as_view()),
            ])),
        
        ]
    )),
    
]