# Generated by Django 4.2.1 on 2023-05-14 12:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('5eef1f17-47f4-4621-b433-9a0312cefaba')),
        ),
    ]
