# Generated by Django 4.2.3 on 2023-10-31 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_details_product_disponibilidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Price'),
        ),
    ]
