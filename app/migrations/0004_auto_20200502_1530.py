# Generated by Django 3.0.5 on 2020-05-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_film_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.PositiveSmallIntegerField(default=2019, verbose_name='Дата выхода'),
        ),
    ]
