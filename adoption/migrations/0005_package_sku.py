# Generated by Django 3.2.6 on 2021-09-20 16:17

import adoption.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0004_package_adoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='sku',
            field=models.CharField(default=adoption.models.generate_sku, editable=False, max_length=12, unique=True),
        ),
    ]
