from django.urls import path
from . import views
from accounts import views as AccountView



urlpatterns = [
    path('', AccountView.teacher_dashboard, name='teacher'),
    path('profile/', views.teacher_profile, name='teach_profile'),
    path('course_builder/', views.course_builder, name='course_builder'),
    path('course_builder/category/<int:pk>/', views.course_by_category, name='course_by_category'),
    path('course_builder/category/course/<int:pk>/', views.section_by_course, name='section_by_course'),
    path('course_builder/category/course/section/<int:pk>/', views.video_by_section, name='video_by_section'),
    
    
    path('course_builder/category/add/', views.add_category, name='add_category'),
    path('course_builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('course_builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    
    path('course_builder/section/add/', views.add_section, name='add_section'),
    path('course_builder/section/edit/<int:pk>/', views.edit_section, name='edit_section'),
    path('course_builder/section/delete/<int:pk>/', views.delete_section, name='delete_section'),
    
    
    path('course_builder/course/add/', views.add_course, name='add_course'),
    path('course_builder/course/edit/<int:pk>/', views.edit_course, name='edit_course'),
    path('course_builder/course/delete/<int:pk>/', views.delete_course, name='delete_course'),
    
    path('course_builder/video/add/', views.add_video, name='add_video'),
    path('course_builder/video/edit/<int:pk>/', views.edit_video, name='edit_video'),
    path('course_builder/video/delete/<int:pk>/', views.delete_video, name='delete_video'),
    
    
]