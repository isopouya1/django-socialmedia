# Generated by Django 4.2.1 on 2023-05-14 13:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_images_alter_profile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('322c7490-5555-483b-b256-8e7f1ab1744a')),
        ),
    ]
