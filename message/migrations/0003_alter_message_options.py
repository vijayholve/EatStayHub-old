# Generated by Django 5.0.6 on 2024-07-09 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['id']},
        ),
    ]