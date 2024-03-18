from django.contrib import admin
from .models import Measurement, HydroponicsSystem


admin.site.register(Measurement)
admin.site.register(HydroponicsSystem)