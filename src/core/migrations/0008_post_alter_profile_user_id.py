# Generated by Django 4.2.1 on 2023-06-02 07:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_nickname_alter_profile_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='image-post')),
                ('caption', models.TextField()),
                ('dtime', models.DateTimeField(auto_now_add=True)),
                ('no_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('48ccd68d-772a-4a45-8f5a-ab5c94f16a19')),
        ),
    ]
