# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='url',
        ),
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='stuff', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(help_text='Enter the general food category (e.g. Mexican, American, Thai, etc)', max_length=50),
        ),
    ]
