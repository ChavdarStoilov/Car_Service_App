from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from .forms import CustomerUserCreation, UserChangeForm

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('username',)
    
    readonly_fields = ["date_joined", 'date_modified',]

    
    list_display = [
        'username',
        'date_joined',
        'date_modified',
        'is_staff',
        'is_active',
        'is_customer',
    ]
    
    list_filter = (
        
    )
    
    add_form = CustomerUserCreation
    form = UserChangeForm
    
    fieldsets = (
        (
            None, 
            {
                "fields": ("username", "is_customer", )
            }
        ),
    )