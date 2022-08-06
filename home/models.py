from email.policy import default
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
        
class PublicPost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.IntegerField() 
    image = models.ImageField(upload_to='images/')
    other_image1 = models.ImageField(upload_to='images/', blank=True)
    other_image2 = models.ImageField(upload_to='images/', blank=True)
    other_image3 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

class ShelterAddress(models.Model):
    post_id = models.ForeignKey(PublicPost, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    pincode = models.IntegerField(6)

    def __str__(self):
        return self.post_id.title
    
class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=13)

    def __str__(self):
        return self.user_id.username
        