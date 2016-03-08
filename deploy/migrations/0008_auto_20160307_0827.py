# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0007_auto_20160307_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='base_name',
            new_name='bash_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='base_path',
            new_name='bash_path',
        ),
    ]
