# Generated by Django 4.2.16 on 2024-12-10 10:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number. Up to 15 digits allowed.', regex='^\\+?1?\\d{9,15}$')])),
                ('contact_email', models.EmailField(max_length=250)),
                ('contact_message', models.TextField(max_length=500)),
            ],
        ),
    ]
