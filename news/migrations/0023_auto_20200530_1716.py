# Generated by Django 3.0.6 on 2020-05-30 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20200530_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlecomment',
            old_name='parent',
            new_name='id_parent',
        ),
    ]
