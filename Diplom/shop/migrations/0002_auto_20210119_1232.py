# Generated by Django 3.1.5 on 2021-01-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=184.53, upload_to='products/%Y/%m/%d', width_field=388),
        ),
    ]
