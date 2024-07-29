from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Sum
from teacher.models import *
from courses.models import *




def course_list(request):
    courses = Course.objects.select_related('teacher').all()
    context = {
        'courses': courses
    }
    return render(request, 'lectures/course_list.html', context)


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    # print(f"Retrieved course: {course}")
    sections = Section.objects.filter(course=course).prefetch_related('videos')
    # print(f"Retrieved sections: {sections}")
    section_data = []
    
    total_lessons = 0
    total_duration = 0
    for section in sections:
        videos = section.videos.all()
        section_total_duration = sum(video.get_duration() for video in videos)  # Ensure this line runs properly
        total_lessons += videos.count()
        total_duration += section_total_duration
        
        section_data.append({
            'section': section,
            'section_total_duration': section_total_duration,
            'videos': videos,
        })
        
        # if total_duration >= 60:
        #     if total_duration >= 3600:
        #         display_duration = total_duration / 3600
        #         duration_unit = "hours"
        #     else:
        #         display_duration = total_duration / 60
        #         duration_unit = "minutes"
        # else:
        #     display_duration = total_duration
        #     duration_unit = "seconds"
        
    context = {
        'course': course,
        'sections': section_data,
        'total_lessons': total_lessons,
        'total_duration': total_duration,
        # 'display_duration': display_duration,
        # 'duration_unit': duration_unit,
    }
    return render(request, 'lectures/course_detail.html', context)