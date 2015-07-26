# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('home_phone', models.IntegerField(max_length=10, blank=True)),
                ('cell_phone', models.IntegerField(max_length=10, blank=True)),
                ('email', models.EmailField(max_length=25, blank=True)),
                ('full_address', models.CharField(max_length=25)),
                ('alt_address', models.CharField(max_length=25, blank=True)),
                ('city', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=12)),
                ('zip_code', models.IntegerField(max_length=5)),
            ],
        ),
    ]
