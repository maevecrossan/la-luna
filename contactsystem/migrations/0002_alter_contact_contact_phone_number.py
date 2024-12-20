# Generated by Django 4.2.16 on 2024-12-16 20:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.                 Up to 15 digits allowed.', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
