# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0009_auto_20160308_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='bash_name',
            new_name='bash_script_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='bash_path',
            new_name='bash_script_path',
        ),
    ]
