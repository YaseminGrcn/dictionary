# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 11:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Olu\u015fturulma Zaman\u0131')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='G\xfcncellenme Zaman\u0131')),
                ('title', models.CharField(max_length=255, verbose_name='Yorum')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Olu\u015fturulma Zaman\u0131')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='G\xfcncellenme Zaman\u0131')),
                ('title', models.CharField(max_length=255, verbose_name='Yorum Basligi')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.CommentTitle', verbose_name='Yorum Basligi'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanici'),
        ),
    ]