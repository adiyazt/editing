# Generated by Django 5.0.1 on 2024-05-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.CharField(default='<function uuid4 at 0x0000029D3D133CE0>', max_length=64, primary_key=True, serialize=False)),
                ('dir', models.CharField(blank=True, max_length=64)),
                ('user_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(default='<function uuid4 at 0x0000029D3D133CE0>', max_length=64, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]