# Generated by Django 3.0.6 on 2020-05-30 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20200530_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='id_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.ArticleComment', verbose_name='Родитель'),
        ),
    ]
