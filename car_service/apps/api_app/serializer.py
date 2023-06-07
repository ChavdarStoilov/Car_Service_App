from ..service_app.models import Cars
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            'model',
            'year',
            'VIN',
            'kilometers',
        ]