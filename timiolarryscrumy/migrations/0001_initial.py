# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(default=b'', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScrumyGoal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goal_name', models.CharField(default=b'', max_length=50)),
                ('goal_id', models.IntegerField(default=10)),
                ('created_by', models.CharField(default=b'', max_length=50)),
                ('moved_by', models.CharField(default=b'', max_length=50)),
                ('owner', models.CharField(default=b'', max_length=50)),
                ('goal_status', models.ForeignKey(to='timiolarryscrumy.GoalStatus', on_delete=django.db.models.deletion.PROTECT)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moved_by', models.CharField(default=b'', max_length=50)),
                ('created_by', models.CharField(default=b'', max_length=50)),
                ('moved_from', models.CharField(default=b'', max_length=50)),
                ('moved_to', models.CharField(default=b'', max_length=50)),
                ('time_of_action', models.TimeField()),
                ('goal', models.ForeignKey(to='timiolarryscrumy.ScrumyGoal', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
