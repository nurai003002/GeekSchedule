from django.contrib import admin

from apps.base import models
# Register your models here.

admin.site.register(models.Settings)
admin.site.register(models.Slide)
admin.site.register(models.Direction)
admin.site.register(models.Group)
admin.site.register(models.Teachers)
admin.site.register(models.Best)
