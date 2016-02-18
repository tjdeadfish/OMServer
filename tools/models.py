# --*-- coding:utf-8 --*--

from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

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
    server_external_ip = forms.IPAddressField(label="外网IP地址", error_messages={ 'required': u'外网ip地址不能为空' })
    server_os = forms.CharField(label="服务器操作系统", error_messages={'request': u'操作系统不能为空'})
    server_admin = forms.CharField(label="服务器管理员", error_messages={'request': u'系统管理员不能为空'})
    server_password = forms.CharField(label="服务器管理密码", error_messages={'request': u'密码不能为空'})
    server_ssh_port = forms.IntegerField(label="服务器ssh端口", error_messages={'request': u'ssh端口不能为空'})
    server_hostname = forms.CharField(label="服务器主机名", error_messages={'request': u'主机名不能为空'})
    provider = forms.CharField(label="供应商")

class ContactForm(ModelForm):
  class Meta:
    model = ServerList
    fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label=u"用户名", error_messages={'required': '请输入用户名'},
                               widget=forms.TextInput(attrs={'placeholder':u"用户名",}),)
    password = forms.CharField(label=u"密码", error_messages={'required': u'请输入密码'},
                               widget=forms.PasswordInput(attrs={'placeholder':u"密码",}),)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=u'原密码', error_messages={'required': u'请输入原密码'},
                                  widget=forms.PasswordInput(attrs={'placeholder':u'原密码',}),)
    new_password = forms.CharField(label=u'新密码', error_messages={'required': u'请输入新密码'},
                                  widget=forms.PasswordInput(attrs={'placeholder': u'新密码'}),)
    verify_password = forms.CharField(label=u'确认密码', error_messages={'required': u'请再一次输入新密码'},
                                      widget=forms.PasswordInput(attrs={'placeholder': u'确认密码',}),)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'所有项都为必填')
        elif self.cleaned_data['new_password'] <> self.cleaned_data['verify_password']:
            raise forms.ValidationError(u'输入密码不一致')
        else:
            cleaned_data = super(ChangePasswordForm, self).clean()
        return cleaned_data
