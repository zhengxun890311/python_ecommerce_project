# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-28 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_auto_20190226_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_info',
            name='Upper_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='upper_category', to='product_app.Upper_category'),
            preserve_default=False,
        ),
    ]
