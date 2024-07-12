from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.my_account, name='my_account'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    
    path('my_account/', views.student_dashboard, name='my_account'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    
    
    path('teacher/', include('teacher.urls'))
]