from django.contrib import admin
from .models import CarQueue, EmployeesProfile, Cars, RepairHistory, CarBrand
# Register your models here.

@admin.register(EmployeesProfile)
class PersonalProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Cars)
class PersonalProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(RepairHistory)
class PersonalProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(CarQueue)
class CarQueueAdmin(admin.ModelAdmin):
    pass

@admin.register(CarBrand)
class CarQueueAdmin(admin.ModelAdmin):
    pass