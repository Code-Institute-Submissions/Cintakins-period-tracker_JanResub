# Generated by Django 4.1.1 on 2022-09-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_colors',
            field=models.CharField(blank=True, choices=[], max_length=10, null=True),
        ),
    ]