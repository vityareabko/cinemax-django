# Generated by Django 3.0.6 on 2020-05-26 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20200526_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecomment',
            name='id_article_reply_comment',
        ),
        migrations.RemoveField(
            model_name='articlecomment',
            name='id_parent',
        ),
    ]
