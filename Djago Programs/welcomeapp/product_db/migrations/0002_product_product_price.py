# Generated by Django 5.1 on 2024-08-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
