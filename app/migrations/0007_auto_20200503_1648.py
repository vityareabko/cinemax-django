# Generated by Django 3.0.5 on 2020-05-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200502_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='url_trailer',
            field=models.SlugField(default='null', max_length=200),
        ),
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(upload_to='actors/'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(upload_to='posters/'),
        ),
    ]
