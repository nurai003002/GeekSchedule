# Generated by Django 5.0.2 on 2024-02-26 15:45

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Best',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_best_who/', verbose_name='Фотография ')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Лучшая за месяц',
                'verbose_name_plural': 'Лучшие за месяц',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='image_logo/', verbose_name='Логотип')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('facebook', models.URLField(verbose_name='facebook URL')),
                ('instagram', models.URLField(verbose_name='instagram URL')),
                ('youtube', models.URLField(verbose_name='youtube URL')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='main_image/', verbose_name='Фотография ')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_teacher/', verbose_name='Фотография Препода')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('work', models.CharField(max_length=255, verbose_name='Дожность')),
            ],
            options={
                'verbose_name': 'Препод',
                'verbose_name_plural': 'Преподы',
            },
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255, verbose_name='Время урока')),
                ('teacher', models.CharField(max_length=255, verbose_name='Преподователь ')),
                ('mentor', models.CharField(max_length=255, verbose_name='Ассистент, Ментор')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_class', to='base.group')),
            ],
            options={
                'verbose_name': 'Расписание Урокa',
                'verbose_name_plural': 'Расписание Уроков',
            },
        ),
    ]