# Generated by Django 3.0.6 on 2020-06-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20200531_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsemovieinfo',
            name='full_describe_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parsemovieinfo',
            name='full_describe_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parsemovieinfo',
            name='short_describe_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parsemovieinfo',
            name='short_describe_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='parsemovieinfo',
            name='title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='parsemovieinfo',
            name='title_uk',
            field=models.CharField(max_length=300, null=True),
        ),
    ]