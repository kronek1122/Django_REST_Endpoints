from rest_framework import serializers
from .models import HydroponicsSystem, Measurement


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicsSystem
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'