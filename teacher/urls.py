from django.urls import path
from . import views
from accounts import views as AccountView



urlpatterns = [
    path('', AccountView.teacher_dashboard, name='teacher'),
    path('profile/', views.teacher_profile, name='teach_profile'),
]