# Generated by Django 3.2.6 on 2021-09-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='apartment_no',
        ),
        migrations.AddField(
            model_name='order',
            name='street_address_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
