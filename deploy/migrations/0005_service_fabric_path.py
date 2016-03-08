# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0004_auto_20160304_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='fabric_path',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
    ]
