from ..service_app.models import Cars, CarQueue, RepairHistory, CustomerProfile
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'model',
            'year',
            'VIN',
            'kilometers',
            'have_history',
        ]
    
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'
        
class CarQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarQueue
        fields = [
            'status',
        ]
        
        
class RepairHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairHistory
        fields = [
            'history',
        ]