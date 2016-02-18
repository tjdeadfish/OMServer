# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverlist',
            name='provider',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
