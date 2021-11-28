from django import forms
from weather.models import WeatherStatus

class SearchAPIForm(forms.ModelForm):
    class Meta:
        model = WeatherStatus
        fields = '__all__'