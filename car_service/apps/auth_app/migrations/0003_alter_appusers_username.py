# Generated by Django 4.2.1 on 2023-07-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_appusers_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusers',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
