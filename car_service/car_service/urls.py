"""
URL configuration for car_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
