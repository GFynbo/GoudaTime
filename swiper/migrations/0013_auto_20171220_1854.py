# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0012_auto_20171220_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='Boston, MA', help_text='123 Sample St, City ST 90210', max_length=125),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location_lat',
            field=models.DecimalField(decimal_places=6, default=42.3601, max_digits=9),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location_lon',
            field=models.DecimalField(decimal_places=6, default=-71.0589, max_digits=9),
        ),
    ]