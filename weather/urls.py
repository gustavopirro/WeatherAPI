from weather.views import ApiViewerTemplate, SearchTestView, WeatherAPIView, WeathersAPIView
from django.urls import path

urlpatterns = [
    path('', ApiViewerTemplate.as_view(), name='homepage'),
    path('weathers/', WeathersAPIView.as_view(), name='weather_list'),
    path('weathers/<int:pk>/', WeatherAPIView.as_view(), name='weather'),
    path('search/', SearchTestView.as_view(), name='test'),

]