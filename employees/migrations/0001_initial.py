# Generated by Django 4.1.5 on 2023-01-23 03:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('close_profile', models.BooleanField(default=False)),
                ('in_active_search', models.BooleanField(default=True)),
            ],
        ),
    ]