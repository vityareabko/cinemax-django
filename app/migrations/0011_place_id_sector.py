# Generated by Django 3.0.5 on 2020-05-05 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200504_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='id_sector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Sector'),
            preserve_default=False,
        ),
    ]
