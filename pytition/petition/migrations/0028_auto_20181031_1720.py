# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-31 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0027_auto_20181031_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateownership',
            name='organization',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='petition.Organization'),
        ),
        migrations.AlterField(
            model_name='templateownership',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='petition.PytitionUser'),
        ),
    ]
