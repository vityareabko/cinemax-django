# Generated by Django 3.0.6 on 2020-05-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20200526_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='id_article_reply_comment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
