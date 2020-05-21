# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timiolarryscrumy', '0002_auto_20200516_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumygoals',
            name='id',
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
