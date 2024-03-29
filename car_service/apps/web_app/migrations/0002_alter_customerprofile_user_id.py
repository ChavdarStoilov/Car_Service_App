# Generated by Django 4.2.1 on 2023-07-04 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='user_id',
            field=models.OneToOneField(limit_choices_to={'is_customer': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
