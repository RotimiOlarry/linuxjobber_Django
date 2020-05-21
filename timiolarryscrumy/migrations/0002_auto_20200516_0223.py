# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timiolarryscrumy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goal_name', models.CharField(default=b'', max_length=50)),
                ('goal_id', models.IntegerField(default=10)),
                ('created_by', models.CharField(default=b'', max_length=50)),
                ('moved_by', models.CharField(default=b'', max_length=50)),
                ('owner', models.CharField(default=b'', max_length=50)),
                ('goal_status', models.ForeignKey(to='timiolarryscrumy.GoalStatus', on_delete=django.db.models.deletion.PROTECT)),
                ('user', models.ForeignKey(related_name=b'goal_created', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='scrumygoal',
            name='goal_status',
        ),
        migrations.RemoveField(
            model_name='scrumygoal',
            name='user',
        ),
        migrations.AlterField(
            model_name='scrumyhistory',
            name='goal',
            field=models.ForeignKey(to='timiolarryscrumy.ScrumyGoals', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.DeleteModel(
            name='ScrumyGoal',
        ),
    ]
