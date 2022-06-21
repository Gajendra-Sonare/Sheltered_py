from home.models import User, PublicPost
from django.http import HttpResponse, JsonResponse
import json, jwt

from home.tools.dashboard import SECRET_KEY

SECRET_KEY = 'django-insecure-62v%tmc%)l1hwv8y^jcyg9hi+92%j49%dpbe4hntsagi(=m89p'
def Post(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        token = data['token']
        post_id = data['post_id']
        # validate the jwt token
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except:
            # return error response if token is invalid
            return JsonResponse({'error': 'Invalid token'}, status=401)
        # get the post using post_id 
        post = PublicPost.objects.get(id=post_id)
        # return post to appropriate formate
        return JsonResponse({
            'title': post.title,
            'price': post.price,
            'description': post.description,
            'image': post.image.url,
        })
