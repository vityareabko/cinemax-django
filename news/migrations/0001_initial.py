# Generated by Django 3.0.6 on 2020-05-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParseMovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=50)),
                ('subscribe', models.TextField()),
                ('url', models.SlugField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
