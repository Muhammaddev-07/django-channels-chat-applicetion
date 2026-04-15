from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    owner_user=models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.
