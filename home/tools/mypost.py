from home.models import User, PublicPost
from django.http import HttpResponse, JsonResponse
import json, jwt

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p'

def Mypost(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        token = data['token']
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(user_id = decoded_token['user_id']) 

        allpost = [] 
        post = PublicPost.objects.filter(user_id = user)
        for obj in post:
            other_image1 = obj.other_image1.url if obj.other_image1 else None
            other_image2 = obj.other_image2.url if obj.other_image2 else None
            other_image3 = obj.other_image3.url if obj.other_image3 else None
            allpost.append([
                obj.id,
                obj.title,
                obj.price,
                obj.description,
                obj.image.url,
                other_image1,
                other_image2,
                other_image3,
            ])

        return JsonResponse(allpost, safe=False)
    return HttpResponse("nothing here")
