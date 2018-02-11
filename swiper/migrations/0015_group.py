# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 21:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swiper', '0014_userprofile_has_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_four', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user_four', to=settings.AUTH_USER_MODEL)),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user_one', to=settings.AUTH_USER_MODEL)),
                ('user_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user_three', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user_two', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
