from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib.auth import get_user_model
#Create your models here.

User = get_user_model()

class CommentManager(models.Manager):
    def withcontent(self):
        return self.filter

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_id = models.UUIDField(default=uuid.uuid4())
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=90,blank=True)
    dtime = models.DateField(auto_now_add=True)
    images = models.ImageField(upload_to="user-image",default='defaulet-avatar.jpg')
    nickname = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self) -> str:
        return self.username.username
        
    def Image(self):
        return format_html("<img width=90 height=90 style='border-radius:5px;' src='{}'>".format(self.images.url))

class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=80)
    image = models.ImageField(upload_to="image-post")
    caption = models.TextField()
    dtime = models.DateTimeField(auto_now_add=True)
    no_likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.user


class Like(models.Model):
    post_id = models.CharField(max_length=50)
    user = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.post_id


class Comment(models.Model):
    author = models.CharField(max_length=90)
    slug = models.CharField(max_length=90,unique=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user = models.CharField(max_length=90)
    comment = models.TextField()

    def __str__(self) -> str:
        return f"{self.author} commented for {self.user}"

