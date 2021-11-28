from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse
from weather.models import WeatherStatus
from .serializers import WeatherSerializer
from rest_framework import generics
from weather.forms import SearchAPIForm
import threading
import datetime, time, requests, random
from django.views.generic import ListView
from django.http import Http404


class SearchTestView(ListView):
    model = WeatherStatus
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_type = self.request.GET.get('q_type')
        
        if search_type == 'id':
            object_list = WeatherStatus.objects.filter(pk=query)
        elif search_type == 'data':
            object_list = WeatherStatus.objects.filter(pk=query)
        else:
            raise Http404('Not found')


        return object_list


class ApiViewerTemplate(TemplateView):
    template_name = 'api_viewer.html'

    def get(self, request):
        api_search_form = SearchAPIForm()
        last_registered_weather = WeatherStatus.objects.last()
        context = {'last_weather': last_registered_weather, 'api_search': api_search_form}
        
        return render(request, self.template_name, context)


class WeathersAPIView(generics.ListCreateAPIView):
    queryset = WeatherStatus.objects.all()
    serializer_class = WeatherSerializer


class WeatherAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherStatus.objects.all()
    serializer_class = WeatherSerializer


class WeatherCollectorThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.luminosity = 0
        self.temperature = 0
        self.humidity = 0
        self.base_url = 'http://127.0.0.1:8000'

    def run(self):
        while True:
            self.temperature = random.randrange(1, 50)
            self.luminosity = random.randrange(1000, 5000, 1000)
            self.humidity = random.randrange(1, 100)
            self.data = {
                "temperature": self.temperature, 
                "luminosity": self.luminosity,
                "humidity": self.humidity 
                }
            try:
                response = requests.post(
                    self.base_url + reverse('weather_list'), self.data)
                time.sleep(10)
            except:
                print('Error has ocurred')
    
weather_collector_thread = WeatherCollectorThread()
weather_collector_thread.start()
        

