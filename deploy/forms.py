# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    script_file = forms.FileField(label=u'Select a file', help_text='max. 42 megabytes')
