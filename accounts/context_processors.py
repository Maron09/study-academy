from teacher.models import *
from django.conf import settings

def get_teacher(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except:
        teacher = None
    return dict(teacher=teacher)


def get_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except:
        user_profile = None
    return dict(user_profile=user_profile)