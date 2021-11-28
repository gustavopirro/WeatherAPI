from rest_framework import serializers
from weather.models import WeatherStatus


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStatus
        fields = '__all__'
