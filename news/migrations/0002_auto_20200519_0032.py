# Generated by Django 3.0.6 on 2020-05-18 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parsemovieinfo',
            old_name='subscribe',
            new_name='describe',
        ),
    ]
