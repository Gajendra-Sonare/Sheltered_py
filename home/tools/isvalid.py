from base64 import decode
from logging import exception
from django.http import request, HttpResponse
import jwt, json

def isValid(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        data = json.loads(data) 
        token = data['token']
        
        try:
            decoded_data = jwt.decode(token, 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p', algorithms=['HS256'])
            return HttpResponse(status = 200)

        except Exception as e:
            return HttpResponse(status = 401)

    return HttpResponse("nothing here")