from .models import *


def get_teacher(request):
    teacher = Teacher.objects.get(user=request.user)
    return teacher