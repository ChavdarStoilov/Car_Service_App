from django.contrib import admin
from .models import CarQueue, EmployeesProfile, Cars, RepairHistory, CarBrand, ServiceGallery

@admin.register(EmployeesProfile)
class EmployeesProfileAdmin(admin.ModelAdmin):
    empty_value_display = "unknown"
    ordering = ('user_id',)
    
    list_display = [
        'user_id',
        "__str__",
    ]

    
    list_filter = (
        'user_id',
    )
    
    list_per_page = 10

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    ordering = ('brand',)
    
    list_display = [
        '__str__',
        "year",
        'VIN',
        'repair',
        'have_history',
        'user_id',
        
    ]

    list_filter = (
        'brand',
    )
    
    list_per_page = 20

@admin.register(RepairHistory)
class RepairHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'car_id',
    ]
    
    list_per_page = 20

    


@admin.register(CarQueue)
class CarQueueAdmin(admin.ModelAdmin):
    ordering = (
        'status',
    )
    
    list_display = [
        'car_id',
        "mechanic_id",
        'status',

        
    ]
    
    list_filter = (
        'status',
    )
    
    list_per_page = 10

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceGallery)
class GalleryAdmin(admin.ModelAdmin):
    pass