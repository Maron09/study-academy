from django.shortcuts import render, redirect, get_object_or_404
from accounts.views import *
from orders.models import *



@login_required(login_url='login')
@user_passes_test(check_role_student)
def student_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserInfoForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('stud_profile')
        else:
            print(profile_form.errors)
            print(user_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)
    
    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'profile': profile,
    }
    return render(request, 'students/stud_profile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_student)
def learning(request):
    my_courses = Enrollment.objects.filter(student=request.user).select_related('course')
    
    context = {
        'my_courses': my_courses
    }
    return render(request, 'students/learning.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_student)
def my_course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    enrollment = get_object_or_404(Enrollment, student=request.user, course=course)
    
    # Get sections with related videos
    sections = Section.objects.filter(course=course).prefetch_related('videos').order_by('order')

    total_lessons = 0
    total_duration = 0

    for section in sections:
        videos = section.videos.all()
        section_total_duration = sum(video.get_duration() for video in videos)  # Calculate total duration for the section
        section.section_total_duration = section_total_duration  # Add total duration to the section
        total_lessons += videos.count()
        total_duration += section_total_duration

    context = {
        'course': course,
        'sections': sections,
        'total_lessons': total_lessons,
        'total_duration': total_duration,
    }
    
    return render(request, 'students/my_course_detail.html', context)

# @login_required(login_url='login')
# def watch_video(request, course_slug, section_id, video_id):
#     course = get_object_or_404(Course, slug=course_slug)
#     enrollment = get_object_or_404(Enrollment, student=request.user, course=course)
    
#     video = get_object_or_404(Video, section__id=section_id, id=video_id)
    
#     context = {
#         'course': course,
#         'video': video,
#     }
#     return render(request, 'students/watch.html', context)