# --*-- coding:utf-8 --*--

from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput,BootstrapTextInput,BootstrapUneditableInput

# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField(label=u"用户名", error_messages={'required': u'请输入用户名'},
                               widget=forms.TextInput(attrs={'placeholder': u"用户名",}),)
    password = forms.CharField(label=u"密码", error_messages={'required': u'请输入密码'},
                               widget=forms.PasswordInput(attrs={'placeholder': u"密码",}),)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=u'原密码', error_messages={'required': u'请输入原密码'},
                                   widget=forms.PasswordInput(attrs={'placeholder': u'原密码',}),)
    new_password = forms.CharField(label=u'新密码', error_messages={'required': u'请输入新密码'},
                                   widget=forms.PasswordInput(attrs={'placeholder': u'新密码'}),)
    verify_password = forms.CharField(label=u'确认密码', error_messages={'required': u'请再一次输入新密码'},
                                      widget=forms.PasswordInput(attrs={'placeholder': u'确认密码',}),)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'所有项都为必填')
        elif self.cleaned_data['new_password'] != self.cleaned_data['verify_password']:
            raise forms.ValidationError(u'输入密码不一致')
        else:
            cleaned_data = super(ChangePasswordForm, self).clean()
        return cleaned_data
