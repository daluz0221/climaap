import requests
import json

from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from Weather.settings import API_KEY

from django.views.generic import (
    TemplateView
)

# Create your views here.


class Home(TemplateView):
    template_name = 'data/index.html'



    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        city = self.request.GET.get('kword', '')

        WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid='+ API_KEY + '&lang=es'

        resp = requests.get(WEATHER_API_URL)
        print(dir(resp))
        print(resp.json())

        if resp.status_code != 200:
            context['data'] = 'ERROR_GET ' + WEATHER_API_URL + ' {}'.format(resp.status_code)

            
        context['data'] = resp.json()

        data = {
            'country': str(context['data']['sys']['country']),
            'longitud' : str(context['data']['coord']['lon']),
            'latitud': str(context['data']['coord']['lat']),
            'temp': str(context['data']['main']['temp']),
            'pressure': str(context['data']['main']['pressure']),
            'humedad': str(context['data']['main']['humidity']),
            'main': str(context['data']['weather'][0]['main']),
            'desc': str(context['data']['weather'][0]['description']),
            'icon': str(context['data']['weather'][0]['icon']),
        }

        context['info'] = data
        # print(context['data'])

        return context
