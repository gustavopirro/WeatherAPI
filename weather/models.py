from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class WeatherStatus(Base):
    temperature = models.IntegerField()
    humidity = models.CharField(max_length=10)
    luminosity = models.IntegerField()
