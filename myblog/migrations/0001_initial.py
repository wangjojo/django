# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=16, verbose_name='作者')),
                ('content', models.TextField(help_text='博客内容', verbose_name='内容')),
                ('pub', models.DateField(auto_now_add=True, verbose_name='发布时间')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
            },
        ),
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='称呼')),
                ('content', models.CharField(max_length=240, verbose_name='内容')),
                ('pub', models.DateField(auto_now_add=True, verbose_name='发布时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.BlogPost', verbose_name='博客')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categroy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Categroy', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(to='myblog.Tag', verbose_name='标签'),
        ),
    ]
