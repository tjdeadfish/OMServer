# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20160304_1106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='task_name',
            new_name='script_task',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='soft_name',
        ),
    ]
