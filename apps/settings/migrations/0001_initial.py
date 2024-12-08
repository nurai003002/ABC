# Generated by Django 5.0.6 on 2024-12-07 15:57

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, default='no_image.jpg', force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='URL facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='URL instagram')),
            ],
            options={
                'verbose_name': 'Основные настройки',
                'verbose_name_plural': 'Основные настройки',
            },
        ),
    ]
