# Generated by Django 3.0.5 on 2020-05-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_actor_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='price',
        ),
    ]
