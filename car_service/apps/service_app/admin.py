from django.contrib import admin
from .models import CarQueue, PersonalProfile, Cars, RepairHistory
# Register your models here.

@admin.register(PersonalProfile)
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