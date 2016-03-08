# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Service(models.Model):
    soft_name = models.CharField(max_length=50)
    script_type = models.CharField(max_length=50, default="")
    fabric_task = models.CharField(max_length=50, default="")
    fabric_path = models.CharField(max_length=150, default="")
    fabric_script_name = models.CharField(max_length=50, default="")
    local_bash_path = models.CharField(max_length=150, default="")
    local_bash_name = models.CharField(max_length=50, default="")


class UploadFile(models.Model):
    script_file = models.FileField(upload_to='scripts')