from django.shortcuts import render
import requests

def index(request):
    appid = 'd4e54608dafc5d0ba494b7a62832b70e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    city = 'London'
    res = requests.get(url.format(city)).json()
    
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = {'info': city_info}
    return render(request, 'Weather/index.html', context)
