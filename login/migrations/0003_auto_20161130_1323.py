# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161130_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='password',
            new_name='register_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='repeat_password',
            new_name='register_repeat_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='username',
            new_name='register_username',
        ),
    ]
