# Generated by Django 3.0.6 on 2020-05-29 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0014_auto_20200529_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='dislike',
            field=models.ManyToManyField(blank=True, default=None, related_name='dislike_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='LikeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=20)),
                ('id_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.ArticleComment')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DislikeReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=20)),
                ('id_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.ArticleComment')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]