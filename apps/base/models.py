from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Settings(models.Model):
    logo = models.ImageField(
        upload_to='image_logo/',
        verbose_name='Логотип'
    )
    phone = models.CharField(
        max_length =255,
        verbose_name = 'Номер телефона'
    )
    address = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес',
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    facebook = models.URLField(
        verbose_name = 'facebook URL'
    )
    instagram = models.URLField(
        verbose_name = 'instagram URL'
    )
    youtube = models.URLField(
        verbose_name = 'youtube URL'
    )

    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class Slide(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description =RichTextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        upload_to='main_image/',
        verbose_name= 'Фотография '
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class Direction(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class DirectionSchedule(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название напрвления для расписания'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '1) Направление для расписания'
        verbose_name_plural = '1) Направления для расписания'

class WeekSchedule(models.Model):
    direction_choice = models.ForeignKey(DirectionSchedule,related_name='direction_choice', on_delete=models.CASCADE, verbose_name = 'Выбрать направление')
    title = models.CharField(
        max_length = 255,
        verbose_name = 'День недели для расписания'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) День недели '
        verbose_name_plural = '2) Дни недели '



class Group(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название группы'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'



class ClassSchedule(models.Model):
    group = models.ForeignKey(Group, related_name='groups_class', on_delete=models.CASCADE)
    time = models.CharField(
        max_length=255,
        verbose_name = 'Время урока'
    )
    teacher = models.CharField(
        max_length = 255,
        verbose_name= 'Преподователь '
    )
    mentor = models.CharField(
        max_length = 255,
        verbose_name= 'Ассистент, Ментор'
    )

    def __str__(self):
        return self.teacher
    
    class Meta:
        verbose_name = 'Расписание Урокa'
        verbose_name_plural = 'Расписание Уроков'

class Teachers(models.Model):
    image = models.ImageField(
        upload_to='image_teacher/',
        verbose_name='Фотография Препода'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Дожность'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Препод'
        verbose_name_plural = 'Преподы'

class Best(models.Model):
    image = models.ImageField(
        upload_to='image_best_who/',
        verbose_name='Фотография '
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Лучшая за месяц'
        verbose_name_plural  = 'Лучшие за месяц'

    


