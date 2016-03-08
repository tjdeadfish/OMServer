# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_uploadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='version',
        ),
        migrations.AddField(
            model_name='service',
            name='script_type',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='task_name',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='script_file',
            field=models.FileField(upload_to=b'scripts'),
            preserve_default=True,
        ),
    ]
