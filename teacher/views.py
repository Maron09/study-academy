from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from accounts.forms import *
from django.contrib import messages
from accounts.views import *
from .utils import *
from django.template.defaultfilters import slugify
# Create your views here.

@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def teacher_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    teacher = get_object_or_404(Teacher, user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        teacher_form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if profile_form.is_valid() and teacher_form.is_valid():
            profile_form.save()
            teacher_form.save()
            messages.info(request, "Profile update successful")
            return redirect('teach_profile')
        else:
            print(profile_form.errors)
            print(teacher_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        teacher_form = TeacherForm(instance=teacher)
    context = {
        'profile_form': profile_form,
        'teacher_form': teacher_form,
        'profile' : profile,
        'teacher': teacher,
    }
    return render(request, 'teacher/teach_profile.html', context)
