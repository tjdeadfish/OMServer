from django.db import models
from django import forms

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"