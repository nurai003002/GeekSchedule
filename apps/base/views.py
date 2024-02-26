from django.shortcuts import render


from apps.base import models
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    direction = models.Direction.objects.all()
    # classschedule = models.ClassSchedule.objects.latest('id')
    teacher = models.Teachers.objects.all()
    best = models.Best.objects.all()
    return render(request, 'index.html', locals())