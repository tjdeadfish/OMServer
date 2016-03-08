# --*-- coding:utf-8 -*-

from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.


class ServerList(models.Model):
    server_internal_ip = models.IPAddressField(blank=True)
    server_external_ip = models.IPAddressField()
    server_os = models.CharField(max_length=50)
    server_admin = models.CharField(max_length=20)
    server_password = models.CharField(max_length=20)
    server_port = models.IntegerField(max_length=10)
    server_hostname = models.CharField(max_length=20)
    provider = models.CharField(max_length=50, default="")


class ServerListSubmit(forms.Form):
    server_internal_ip = forms.IPAddressField(label="内网IP地址")
    server_external_ip = forms.IPAddressField(label="外网IP地址", error_messages={'required': u'外网ip地址不能为空' })
    server_os = forms.CharField(label="服务器操作系统", error_messages={'required': u'操作系统不能为空'})
    server_admin = forms.CharField(label="服务器管理员", error_messages={'required': u'系统管理员不能为空'})
    server_password = forms.CharField(label="服务器管理密码", error_messages={'required': u'密码不能为空'})
    server_ssh_port = forms.IntegerField(label="服务器ssh端口", error_messages={'required': u'ssh端口不能为空'})
    server_hostname = forms.CharField(label="服务器主机名", error_messages={'required': u'主机名不能为空'})
    provider = forms.CharField(label="供应商")


class ContactForm(ModelForm):
    class Meta:
        model = ServerList
        fields = '__all__'