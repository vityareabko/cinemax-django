# Generated by Django 3.0.6 on 2020-06-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200614_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='contry_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='contry_uk',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
