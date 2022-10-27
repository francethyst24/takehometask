from django.shortcuts import render
import json
import requests
from django.conf import settings

# Create your views here.


def index(request):
    context = {
        'cities_select': fetch_cities(request),
        'weather': fetch_weather(request),
    }
    return render(request, "currentweather/index.html", context)


def fetch_cities(request):
    api_call = requests.get(
        'https://countriesnow.space/api/v0.1/countries/capital'
    )
    api_response = json.loads(api_call.content.decode())
    countries_dict = sorted(
        api_response.get('data'),
        key=lambda d: d['capital'],
    )
    cities_dict = list()
    for country in countries_dict:
        if country['capital']:
            cities_dict.append(country)
    return cities_dict


def fetch_weather(request):
    query = request.GET.get('q')
    if query:
        api_call = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + query.strip()
            + "&APPID=" + settings.WEATHER_API_KEY + "&units=metric"
        )
        api_response = json.loads(api_call.content.decode())
        weather_dict = {
            'city_name': str(api_response['name']) + ", " + str(api_response['sys']['country']),
            'temp': str(api_response['main']['temp']) + ' °C',
            'feels_like': str(api_response['main']['feels_like']) + ' °C',
            'humidity': str(api_response['main']['humidity']) + '%',
        }
        return weather_dict
