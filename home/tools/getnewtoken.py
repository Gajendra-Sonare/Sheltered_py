# get new token from access token 
from django.http import request, HttpResponse
import jwt
import json
import requests

def getNewToken(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data = json.loads(data) 
        token = data['refresh']
        url = "http://localhost:8000/api/token/refresh/"
        
        response = requests.post(url, data={'refresh': token})
        print(response)
        return HttpResponse(response.text)
    return HttpResponse("nothing here")