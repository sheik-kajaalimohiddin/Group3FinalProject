# Generated by Django 3.2.10 on 2023-05-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_property_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='flag',
            field=models.BooleanField(default=True),
        ),
    ]