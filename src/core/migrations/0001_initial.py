# Generated by Django 4.2.1 on 2023-05-14 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(default=uuid.UUID('ca6816d0-0685-47fc-8ba1-1160be4a826b'))),
                ('bio', models.TextField(blank=True)),
                ('address', models.CharField(blank=True, max_length=90)),
                ('dtime', models.DateField(auto_now_add=True)),
                ('img', models.ImageField(default='', upload_to='user-image')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]