# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-27 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lower_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_desc', models.CharField(max_length=500)),
                ('product_gender', models.CharField(max_length=10)),
                ('product_price', models.CharField(max_length=20)),
                ('product_inventory', models.CharField(max_length=20)),
                ('product_path', models.CharField(max_length=200)),
                ('Lower_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='small_category', to='product_app.Lower_category')),
            ],
        ),
        migrations.CreateModel(
            name='Upper_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lower_category',
            name='Upper_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_category', to='product_app.Upper_category'),
        ),
    ]
