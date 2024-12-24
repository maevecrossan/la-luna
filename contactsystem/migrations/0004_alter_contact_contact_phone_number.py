import django.core.validators
from django.db import migrations, models
import contactsystem.models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsystem', '0003_contact_is_resolved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number.                 Between 9 and 15 digits allowed.', regex='^\\+?1?\\d{9,15}$'), contactsystem.models.validate_min_length]),
        ),
    ]
