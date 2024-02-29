# Generated by Django 5.0.2 on 2024-02-29 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название напрвления')),
                ('direction_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='derection_schedule_pluse', to='base.direction')),
            ],
            options={
                'verbose_name': 'Направление для расписания',
                'verbose_name_plural': 'Направления для расписания',
            },
        ),
    ]
