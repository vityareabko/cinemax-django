# Generated by Django 3.0.5 on 2020-05-07 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_sector_price_sector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('time', models.TimeField()),
                ('type_day', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='session',
            name='session_time_start',
        ),
        migrations.AddField(
            model_name='session',
            name='id_time_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Time_Sessions'),
            preserve_default=False,
        ),
    ]
