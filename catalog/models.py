from django.db import models
from django.urls import reverse
import base64
from django import forms
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Item(models.Model):
    item_name = models.CharField(max_length=50, default="Magic powder")
    item_cost = models.IntegerField('Cost', null=False, default='150')
    item_descr = models.TextField(max_length=1000, help_text='Enter a description:', default="It's empty, for a while, but soon some item will be here")
    item_image = models.FileField(upload_to='catalog/static/img/', default='blank.jpg')

    def __str__(self):
        return self.item_name


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


# Create your models here.
