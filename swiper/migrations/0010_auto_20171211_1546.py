# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swiper', '0009_auto_20171210_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='matches',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='manager',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='matches',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='swiper/static/img/no-img.png', upload_to='swiper/static/img/<django.db.models.query_utils.DeferredAttribute object at 0x104743940>'),
        ),
    ]