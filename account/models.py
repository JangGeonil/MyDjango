from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #user = models.OneToOneField(User) # 수정전 
    phone_nuber = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
