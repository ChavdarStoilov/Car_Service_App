# Generated by Django 4.2.1 on 2023-05-31 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0003_carbrand_cars_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='кilometers',
            new_name='kilometers',
        ),
    ]
