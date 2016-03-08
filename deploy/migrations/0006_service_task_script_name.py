# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0005_service_fabric_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='task_script_name',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
