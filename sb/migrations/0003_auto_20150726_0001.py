# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sb', '0002_auto_20150725_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='home_phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(max_length=5),
        ),
    ]
