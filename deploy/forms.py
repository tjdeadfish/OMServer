# -*- coding: utf-8 -*-
from django import forms
from models import Service


class ServiceForm(forms.ModelForm):
    soft_name = forms.CharField(label=u'软件', error_messages={'required': u'服务名不能为空'})
    script_type = forms.CharField(label=u'脚本类型')
    fabric_task = forms.CharField(label=u'fab任务名')
    fabric_path = forms.CharField(label=u'fab脚本路径')
    fabric_script_name = forms.CharField(label=u'fab脚本名')
    local_bash_path = forms.CharField(label=u'本地shell脚本路径')
    local_bash_name = forms.CharField(label=u'shell脚本名')

    class Meta:
        model = Service
        fields = "__all__"


class UploadFileForm(forms.Form):
    script_file = forms.FileField(label=u'Select a file', help_text='max. 42 megabytes')
