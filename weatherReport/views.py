from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import UserForm
from .models import User
from .secrets import *

import requests

def new_user(request):
	if request.POST:
		form = UserForm(request.POST, request.POST)
		if form.is_valid():
			user = form.save()
		return redirect(dashboard, user_id = user.id)
	else:
		return render(request, 'userinfo.html', {'form':UserForm})

def dashboard(request, user_id):
	user = User.objects.get(id = user_id)
	geocode = get_geocode(user.address)
	weather = get_weather(geocode)
	return render(request, "dashboard.html", {'user': user, 'weather': weather})

def get_geocode(address):
	url = 'http://www.mapquestapi.com/geocoding/v1/address'
	params = {'key': mapquest_api_key, 'location': address}
	response = requests.get(url, params=params).json()
	return response['results'][0]['locations'][0]['latLng']


def get_weather(geocode):
	url = 'https://api.openweathermap.org/data/2.5/onecall'
	params = {'appid': openweather_api_key, 'lat': geocode['lat'], 'lon': geocode['lng'], 'units': 'imperial'}
	data = requests.get(url, params=params).json()['current']
	return {'description': data['weather'][0]['description'], 'temp': data['temp'], 'feels_like': data['feels_like']}
