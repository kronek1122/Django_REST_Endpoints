from rest_framework import viewsets

from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from .models import HydroponicsSystem, Measurement


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset =HydroponicsSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset =Measurement.objects.all()
    serializer_class = MeasurementSerializer