from django.db import models
from django.contrib.auth.models import User     # import django default user

# Create your models here.

class Status(models.Model):
    text = models.TextField(max_length=20,default="default text")
    image_link = models.ImageField(upload_to='user_uploads/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)     # django default model

