# Generated by Django 4.0.1 on 2022-03-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_details',
            field=models.TextField(),
        ),
    ]
