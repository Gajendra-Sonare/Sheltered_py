from django.shortcuts import render
from django.http import HttpResponse , request
from django.db import models 
from home.models import PublicPost, User
import json, jwt

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p'

def CreatePost(request):
    if request.method == "POST":
        data = request.POST
        images = request.FILES
        image = request.FILES.get('image')
        other_image1 = images.get('other_image1')
        other_image2 = images.get('other_image2')
        other_image3 = images.get('other_image3')
        title = data['title']
        price = data['price']
        description = data['description']
        token = data['token']
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        try:
            user = User.objects.get(user_id = decoded_token['user_id'])
            user = PublicPost(user_id=user, title=title, price=price, description=description,
                            image=image, other_image1=other_image1, other_image2=other_image2, other_image3=other_image3)
            user.save()
            return HttpResponse("Post created")
        except Exception as e:
            HttpResponse(e)

    return HttpResponse("nothing here") 
