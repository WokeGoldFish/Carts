from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Post, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

