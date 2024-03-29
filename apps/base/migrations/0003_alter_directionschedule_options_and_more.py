# Generated by Django 5.0.2 on 2024-02-29 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_directionschedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directionschedule',
            options={'verbose_name': '1) Направление для расписания', 'verbose_name_plural': '1) Направления для расписания'},
        ),
        migrations.RemoveField(
            model_name='directionschedule',
            name='direction_schedule',
        ),
        migrations.AlterField(
            model_name='directionschedule',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название напрвления для расписания'),
        ),
        migrations.CreateModel(
            name='WeekSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Время для расписания')),
                ('direction_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direction_choice', to='base.directionschedule', verbose_name='Выбрать направление')),
            ],
            options={
                'verbose_name': '2) День недели ',
                'verbose_name_plural': '2) Дни недели ',
            },
        ),
    ]
