# Generated by Django 4.1.1 on 2022-11-22 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userperiodinfo_period_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperiodinfo',
            name='period_start_date',
            field=models.DateField(default=datetime.date(2022, 11, 22)),
        ),
    ]