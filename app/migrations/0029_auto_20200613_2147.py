# Generated by Django 3.0.6 on 2020-06-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20200602_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='spaciousness',
            field=models.IntegerField(default=0),
        ),
    ]
