# Generated by Django 5.0.4 on 2024-07-08 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_vendor_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 15, 5, 35, 33, 78226, tzinfo=datetime.timezone.utc)),
        ),
    ]
