# Generated by Django 3.0.5 on 2020-05-02 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='app.Actor', verbose_name='режиссер'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(related_name='film_actor', to='app.Actor', verbose_name='актеры'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='app.Genre', verbose_name='жанры'),
        ),
    ]
