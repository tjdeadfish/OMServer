# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0006_service_task_script_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='base_name',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='base_path',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
    ]
