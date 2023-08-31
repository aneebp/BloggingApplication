from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=False)
    avatar = models.ImageField(null=True,default='avatar.svg')


class Blogge(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=300,null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-created']    


class Comment(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    blogge = models.ForeignKey(Blogge,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)  


    def __str__(self):
        return self.body[0:50]
    

    class Meta:
        ordering = ['-created']     