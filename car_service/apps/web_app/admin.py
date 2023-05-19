from django.contrib import admin
from .models import CustomerProfile
# Register your models here.

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    pass