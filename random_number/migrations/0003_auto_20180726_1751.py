# Generated by Django 2.0.7 on 2018-07-26 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('random_number', '0002_number_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
