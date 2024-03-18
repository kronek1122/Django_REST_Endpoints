from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'measurement', views.MeasurementViewSet)
routers.register(r'hydroponic_system', views.HydroponicSystemViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
