from django.http import HttpResponse, request
from home.models import PublicPost, ShelterAddress
import json

def deletePost(request):
    print(request)
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print('data', data)
        post_id = data['post_id']
        try:
            post = PublicPost.objects.get(id=post_id)
            post.delete()
            return HttpResponse("Post deleted")
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
    return HttpResponse("nothing here")