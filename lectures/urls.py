from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='lectures'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
]