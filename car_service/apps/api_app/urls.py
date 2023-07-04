from django.urls import path, include
from .views import CarApiVeiw, CarQueueApiVeiw, InvoiceApiView, CustomerApiView


urlpatterns = [
    path('', include([
        path('api-auth/', include('rest_framework.urls')),
        path('car/', include([
            path('<int:pk>/', CarApiVeiw.as_view(), name="car"),            
            path('queue/<int:pk>/', CarQueueApiVeiw.as_view(), name="queue cars"),
            path('history/<int:pk>/', InvoiceApiView.as_view(), name="history"),
            ])),
        ]
    )),
    
]