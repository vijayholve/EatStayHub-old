# Generated by Django 5.0.6 on 2024-06-08 06:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0010_alter_dish_description_alter_dish_dishname_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('roomName', models.CharField(max_length=100)),
                ('roomType', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('roomImage', models.ImageField(upload_to='roomImages')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]