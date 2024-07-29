from django.shortcuts import render
from lectures.views import *




def home(request):
    courses = Course.objects.select_related('teacher').all()[:4]
    context = {
        'courses': courses
    }
    return render(request, 'home.html', context)