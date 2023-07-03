from django.contrib import admin
from .models import CarQueue, EmployeesProfile, Cars, RepairHistory, CarBrand
# Register your models here.

@admin.register(EmployeesProfile)
class EmployeesProfileAdmin(admin.ModelAdmin):
    empty_value_display = "unknown"
    ordering = ('user_id',)
    
    list_display = [
        'user_id',
        "__str__",
        'position',
    ]

    
    list_filter = (
        'user_id',
    )

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

@admin.register(RepairHistory)
class RepairHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'car_id',
    ]


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

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass