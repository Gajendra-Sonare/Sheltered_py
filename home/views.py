from asyncio import exceptions
from pickle import FALSE
from click import password_option
from django import http
from django.shortcuts import render
from django.http import HttpResponse , request, JsonResponse
from django.db import models 
from .models import User
import json, requests, jwt
from django.contrib.auth import authenticate, login


# Create your views here.

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p'

class createAccount(models.Model):
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password

    def registerAccount(self):
        try:
            user = User(username=self.username, name=self.name, password=self.password)
            user.save()
            return 1 
        except Exception as e:
            print(e)
            return 0
        

def mainpage(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data["action"] == "signup":
            username = data["username"]
            name = data["name"]
            password = data["password"]
            user = createAccount(username, name, password)
            if user.registerAccount():
                return HttpResponse("Account created")
            else:
                return HttpResponse("Account already exists")

        elif data["action"] == "login":
            username = data["username"]
            password = data["password"] 
            print(username, password)
            try:
                user = User.objects.get(username=str(username))
                if user.password == password: 
                    print(user.password)
                    jwt_data = requests.post('http://localhost:8000/api/token/', data={'username': user.username, 'password': user.password})
                    return JsonResponse(jwt_data.json(), safe=False) 
                else:
                    return HttpResponse(status=403) 
            except Exception as e:
                return HttpResponse(e)
        else:
            print("not signup or login")
            return HttpResponse("not signup or login")

    else:
        return HttpResponse("Not valid request")
