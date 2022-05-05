from django.db import models
from django.contrib.auth.models import User
#^imported User model from django auth^
#NOT the same class as 'User.py'

from backend.models.User import User as Profile  

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)