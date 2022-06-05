from email.policy import default
from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username 
        
class PublicPost(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.IntegerField() 
    image = models.ImageField(upload_to='images/')
    other_image1 = models.ImageField(upload_to='images/', blank=True)
    other_image2 = models.ImageField(upload_to='images/', blank=True)
    other_image3 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title