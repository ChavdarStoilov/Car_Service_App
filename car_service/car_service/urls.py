
from django.contrib import admin
from django.urls import path, include



admin.site.site_header = 'Service administration'
admin.site.site_title = 'Service administration'
admin.site.index_title = 'Applications administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.web_app.urls')),
    path('service/', include('apps.service_app.urls')),
    path('account/', include('apps.auth_app.urls')),
    path('api/', include('apps.api_app.urls')),
]
