# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('concertowl', '0007_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preview',
            options={'get_latest_by': 'updated_at'},
        ),
        migrations.AddField(
            model_name='preview',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 7, 15, 56, 56, 285319), auto_now=True),
            preserve_default=False,
        ),
    ]