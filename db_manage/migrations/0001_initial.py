# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBase',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('database_name', models.CharField(max_length=30)),
                ('database_ip', models.IPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DBA',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('state_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sql', models.CharField(max_length=2000, null=True, blank=True)),
                ('desc', models.CharField(max_length=2000, null=True, blank=True)),
                ('create_time', models.DateField()),
                ('last_up_time', models.DateField(null=True, blank=True)),
                ('dba_comment', models.CharField(max_length=2000, null=True, blank=True)),
                ('attachment', models.FileField(null=True, upload_to=b'tasks', blank=True)),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('databases', models.ManyToManyField(to='db_manage.DataBase')),
                ('dba', models.ForeignKey(to='db_manage.DBA')),
                ('manager', models.ForeignKey(to='db_manage.Manager')),
                ('state', models.ForeignKey(to='db_manage.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
