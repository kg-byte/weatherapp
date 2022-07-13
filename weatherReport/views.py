from django.shortcuts import render
from django.http import HttpResponse
import requests

def users(requests):
  response = requests.get('https://jsonplaceholder.typicode.com/users')
  users = response.json()
