# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-11 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0015_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='receive_email',
            field=models.BooleanField(default=False),
        ),
    ]