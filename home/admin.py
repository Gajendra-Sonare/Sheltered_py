from django.contrib import admin
from .models import PublicPost, ShelterAddress, UserProfile

# Register your models here.
admin.site.register(ShelterAddress)
admin.site.register(PublicPost)
admin.site.register(UserProfile)