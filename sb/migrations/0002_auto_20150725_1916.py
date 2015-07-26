# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cell_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='home_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
