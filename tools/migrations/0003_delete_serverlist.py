# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_serverlist_provider'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServerList',
        ),
    ]
