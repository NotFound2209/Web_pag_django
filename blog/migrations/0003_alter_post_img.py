# Generated by Django 4.2.3 on 2023-10-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='Blog', verbose_name='Image'),
        ),
    ]
