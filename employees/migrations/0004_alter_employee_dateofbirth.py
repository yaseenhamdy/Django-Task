# Generated by Django 5.1 on 2024-09-22 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_employee_day_remove_employee_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
