from django.contrib import admin
from .models import CustomerProfile
# Register your models here.

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'first_name',
        'last_name',
        'email',
        'phone',   
    )
