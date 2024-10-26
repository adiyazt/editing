# Generated by Django 5.0.1 on 2024-05-15 09:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False),
        ),
    ]
