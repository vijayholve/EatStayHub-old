# Generated by Django 5.0.6 on 2024-07-04 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_dish_hotel_alter_restaurants_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.hotel'),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.hotel'),
        ),
    ]