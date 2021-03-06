# Generated by Django 3.0.6 on 2020-06-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_actor_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='biography_en',
            field=models.TextField(null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='actor',
            name='biography_uk',
            field=models.TextField(null=True, verbose_name='Биография'),
        ),
        migrations.AddField(
            model_name='film',
            name='desc_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='desc_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='name_uk',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_uk',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='name_sector_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='name_sector_uk',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='weekday',
            name='weekday_uk',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='weekday_en',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
