# Generated by Django 5.0.6 on 2024-06-09 17:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_roomimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomNo',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]