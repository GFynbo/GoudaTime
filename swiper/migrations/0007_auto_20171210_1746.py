# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 22:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid

def create_uuid(apps, schema_editor):
    Picture = apps.get_model('swiper', 'Picture')
    for pic in Picture.objects.all():
        pic.uuid = uuid.uuid4()
        device.save()

class Migration(migrations.Migration):

    dependencies = [
        ('swiper', '0006_auto_20171210_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='swiper/static/img/no-img.png', upload_to='swiper/static/img/<django.db.models.fields.UUIDField>'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='swiper/static/img/no-img.png', upload_to='swiper/static/img/<django.db.models.query_utils.DeferredAttribute object at 0x1081fe978>'),
        ),
    ]
