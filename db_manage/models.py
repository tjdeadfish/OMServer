from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)

    def __unicode__(self):
        return self.last_name + self.first_name

class DBA(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)

    def __unicode__(self):
        return self.last_name + self.first_name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.state_name

class DataBase(models.Model):
    id = models.AutoField(primary_key=True)
    database_name = models.CharField(max_length=30)
    database_ip = models.IPAddressField(max_length=30)

    def __unicode__(self):
        return self.database_name + '-' + self.database_ip

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    creater = models.ForeignKey(User)
    manager = models.ForeignKey(Manager)
    dba = models.ForeignKey(DBA)
    state = models.ForeignKey(State)
    databases = models.ManyToManyField(DataBase)
    sql = models.CharField(max_length=2000, blank=True, null=True)
    desc = models.CharField(max_length=2000, blank=True, null=True)
    create_time = models.DateField()
    last_up_time = models.DateField(blank=True, null=True)
    dba_comment = models.CharField(max_length=2000, blank=True, null=True)
    attachment = models.FileField(upload_to='tasks', blank=True, null=True)

    def __unicode__(self):
        return str(self.id)