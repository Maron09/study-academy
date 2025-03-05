from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from accounts.forms import *
from django.contrib import messages
from accounts.views import *
from .utils import *
from django.template.defaultfilters import slugify
from courses.models import *
from courses.forms import *
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



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def course_builder(request):
    teacher = get_teacher(request)
    categories = Category.objects.filter(teacher=teacher).order_by('created_at')
    context = {
        'categories': categories
    }
    return render(request, 'teacher/course_builder.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def course_by_category(request, pk):
    teacher = get_teacher(request)
    category = get_object_or_404(Category, pk=pk)
    course = Course.objects.filter(teacher=teacher, category=category)
    context = {
        'course': course,
        'category': category
    }
    return render(request, 'teacher/course.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.teacher = get_teacher(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category added successfully')
            return redirect('course_builder')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'teacher/add_category.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def edit_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category = form.save(commit=False)
            category.teacher = get_teacher(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('course_builder')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'teacher/category_edit.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def delete_category(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('course_builder')


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course_name = form.cleaned_data['course_name']
            course = form.save(commit=False)
            course.teacher = get_teacher(request)
            course.slug = slugify(course_name)
            form.save()
            messages.success(request, 'Course created Successfully')
            return redirect('course_by_category', course.category.id)
        else:
            print(form.errors)
    else:
        form = CourseForm()
        form.fields['category'].queryset = Category.objects.filter(teacher=get_teacher(request))
    context = {
        'form': form,
    }
    return render(request, 'teacher/add_course.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def section_by_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    section = Section.objects.filter(course=course)
    context = {
        'section': section,
        'course': course,
        'course_name': course.course_name
    }
    return render(request, 'teacher/section.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            # Associate the section with the selected course
            section.save()
            messages.success(request, 'Section created successfully')
            return redirect('section_by_course', section.course.id)
        else:
            print(form.errors)
    else:
        form = SectionForm()
        form.fields['course'].queryset = Course.objects.filter(teacher=get_teacher(request))
    
    context = {
        'form': form,
    }
    return render(request, 'teacher/add_section.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def edit_course(request, pk=None):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            # Save the form data
            form.save()
            messages.success(request, 'Course updated successfully')
            return redirect('course_by_category', course.category.id)
        else:
            print(form.errors)
    else:
        form = CourseForm(instance=course)
    
    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'teacher/course_edit.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def delete_course(request, pk=None):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('course_by_category', course.category.id)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def edit_section(request, pk=None):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            # Save the form data
            form.save()
            messages.success(request, 'Section updated successfully')
            return redirect('section_by_course', section.course.id)
        else:
            print(form.errors)
    else:
        form = SectionForm(instance=section)
    
    context = {
        'form': form,
        'section': section,
    }
    return render(request, 'teacher/edit_section.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def delete_section(request, pk=None):
    section = get_object_or_404(Section, pk=pk)
    section.delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('section_by_course', section.course.id)



@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def video_by_section(request, pk):
    section = get_object_or_404(Section, pk=pk)
    course = section.course
    video = Video.objects.filter(section=section)
    video_data = []
    for vid in video:
        video_data.append({
            'video': vid,
            'duration': vid.get_duration(),
        })
    context = {
        'video_data': video_data,
        'section': section,
        'course': course,
        'section_title': section.section_title
    }
    return render(request, 'teacher/video.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def add_video(request):
    teacher = get_teacher(request)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            # Associate the section with the selected course
            video.save()
            messages.success(request, 'Video Added successfully')
            return redirect('video_by_section', video.section.id)
        else:
            print(form.errors)
    else:
        form = VideoForm()
        form.fields['section'].queryset = Section.objects.filter(course__teacher=teacher)
    
    context = {
        'form': form,
    }
    return render(request, 'teacher/add_video.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def edit_video(request, pk=None):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            # Save the form data
            form.save()
            messages.success(request, 'Video updated successfully')
            return redirect('video_by_section', video.section.id)
        else:
            print(form.errors)
    else:
        form = VideoForm(instance=video)
    
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'teacher/edit_video.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def delete_video(request, pk=None):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('video_by_section', video.section.id)