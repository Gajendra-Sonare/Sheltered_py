from django.contrib import admin
from .models import PublicPost, ShelterAddress

# Register your models here.
admin.site.register(ShelterAddress)
admin.site.register(PublicPost)