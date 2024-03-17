from django.db import models
from django.contrib.auth.models import User


class HydroponicsSystem(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Measurement(models.Model):
    system = models.ForeignKey(HydroponicsSystem, name = 'measurement', on_delete=models.CASCADE)
    pH = models.FloatField()
    water_temp = models.FloatField()
    TDS = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Measurement for {self.system.name} at {self.date}'