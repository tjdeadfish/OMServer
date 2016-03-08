# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0010_auto_20160308_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='bash_script_name',
            new_name='local_bash_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='bash_script_path',
            new_name='local_bash_path',
        ),
    ]
