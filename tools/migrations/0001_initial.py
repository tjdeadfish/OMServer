# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_internal_ip', models.IPAddressField(blank=True)),
                ('server_external_ip', models.IPAddressField()),
                ('server_os', models.CharField(max_length=50)),
                ('server_admin', models.CharField(max_length=20)),
                ('server_password', models.CharField(max_length=20)),
                ('server_port', models.IntegerField(max_length=10)),
                ('server_hostname', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
