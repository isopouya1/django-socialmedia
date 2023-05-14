from django.db import models
import uuid
from django.contrib.auth.models import User


#Create your models here.

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_id = models.UUIDField(default=uuid.uuid4())
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=90,blank=True)
    dtime = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to="user-image",default='')

    def __str__(self) -> str:
        return self.username.username