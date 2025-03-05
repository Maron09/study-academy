from django.urls import path
from . import views
from accounts import views as Accountviews



urlpatterns = [
    path('', Accountviews.student_dashboard, name='student'),
    path('profile/', views.student_profile, name='stud_profile'),
    path('learning/', views.learning, name='learning'),
    # path('watch/<slug:course_slug>/section/<int:section_id>/video/<int:video_id>', views.watch_video, name='watch_video'),
    path('learning/<slug:course_slug>/', views.my_course_detail, name='my_course_detail')
]