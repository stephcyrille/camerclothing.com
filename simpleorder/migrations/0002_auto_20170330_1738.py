# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-30 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleorder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuadress',
            old_name='civilite',
            new_name='secteur',
        ),
        migrations.RemoveField(
            model_name='anuadress',
            name='email',
        ),
        migrations.RemoveField(
            model_name='anuadress',
            name='prenom',
        ),
    ]
