# Generated by Django 3.0.6 on 2020-05-30 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20200529_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='id_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.ArticleComment', verbose_name='Родитель'),
        ),
    ]