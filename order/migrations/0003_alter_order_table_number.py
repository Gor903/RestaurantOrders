# Generated by Django 5.1.5 on 2025-01-20 21:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_order_start_order_until"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="table_number",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
