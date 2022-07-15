from re import A
from home.models import User, PublicPost, ShelterAddress
from django.http import HttpResponse, JsonResponse
import json, jwt

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p' 

def Dashboard(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        # token = data['token']
        # decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        page = data['page']
        allpost = [] 
        post = PublicPost.objects.all()[(page-1) * 4: page*4]
        # get address from ShelterAddress
        for obj in post:
            # get address from the shelteraddress 
            address = ShelterAddress.objects.get(post_id = obj)
            print('land', address.landmark)
            allpost.append([
                obj.title,
                obj.id,
                obj.price,
                obj.description,
                address.landmark,
                address.street,
                address.pincode,
                obj.image.url,
                
            ])

        return JsonResponse(allpost, safe=False)
    return HttpResponse("nothing here")
