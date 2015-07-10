# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150710_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigepuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
