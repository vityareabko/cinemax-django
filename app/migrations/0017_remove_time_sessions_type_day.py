# Generated by Django 3.0.5 on 2020-05-07 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200507_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_sessions',
            name='type_day',
        ),
    ]
