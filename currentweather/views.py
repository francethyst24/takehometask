from django.shortcuts import render
import urllib.request
import json

# Create your views here.


def index(request):
    if request.method == 'POST':

        search = request.POST.get('search')

        search_url = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+search+'&APPID=c27c43c136cff28d8e78c4b47eb57282&units=metric').read()

        convert = json.loads(search_url)
        context = {
            'city_name': str(convert['name']),
            'temp': str(convert['main']['temp']) + ' degree Celsius',
            'feels_like': str(convert['main']['feels_like']) + ' degree Celsius',
            'humidity': str(convert['main']['humidity']) + ' percent',
        }
    else:
        context = {}
        search = ''
    return render(request, "currentweather/index.html", context)
