# Generated by Django 3.0.6 on 2020-06-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20200614_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='premiere',
            field=models.DateField(default=None),
        ),
    ]
