from ..service_app.models import Cars, CarQueue
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'model',
            'year',
            'VIN',
            'kilometers',
            'history_id',
        ]
        
class CarQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarQueue
        fields = [
            'status',
        ]