from asyncio import exceptions
import email
from pickle import FALSE
from click import password_option
from django import http
from django.shortcuts import render
from django.http import HttpResponse , request, JsonResponse
from django.db import models 
import json, requests, jwt
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p'

class createAccount(models.Model):
    def __init__(self, username, name, password, email, mobile):
        self.username = username
        self.name = name
        self.password = password
        self.email = email 
        self.mobile = mobile 

    def registerAccount(self):
        try:
            user = User.objects.create(username=self.username, email = self.email)
            user.set_password(self.password)
            profile = UserProfile(user_id=user, name=self.name, mobile=str(self.mobile))
            user.save()
            profile.save()
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
            email = data["email"]
            mobile = data["mobile"]
            # print(username, name, password, email, mobile)
            user = createAccount(username, name, password, email, mobile)
            if user.registerAccount():
                return HttpResponse("Account created")
            else:
                return HttpResponse("Account already exists")

        elif data["action"] == "login":
            username = data["username"]
            password = data["password"] 
            try:
                user = User.objects.get(username=username)

                if authenticate(username=username, password=password): 
                    jwt_data = requests.post('http://localhost:8000/api/token/', data={'username': username, 'password': password})
                    return JsonResponse(jwt_data.json(), safe=False) 
                else:
                    return HttpResponse(status=401) 
            except Exception as e:
                print(e)
                return HttpResponse(status=401)
        else:
            print("not signup or login")
            return HttpResponse("not signup or login")

    else:
        return HttpResponse("Not valid request")
