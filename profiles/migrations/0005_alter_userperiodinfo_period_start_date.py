# Generated by Django 4.1.1 on 2022-10-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userperiodinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperiodinfo',
            name='period_start_date',
            field=models.DateField(),
        ),
    ]
