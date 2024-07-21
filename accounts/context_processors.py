from teacher.models import *
from django.conf import settings

def get_teacher(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except:
        teacher = None
    return dict(teacher=teacher)