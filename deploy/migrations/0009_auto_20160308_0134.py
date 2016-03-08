# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0008_auto_20160307_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='script_task',
            new_name='fabric_script_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='task_script_name',
            new_name='fabric_task',
        ),
    ]
