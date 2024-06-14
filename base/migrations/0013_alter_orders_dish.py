# Generated by Django 5.0.6 on 2024-06-11 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_orders_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to='base.dish'),
        ),
    ]