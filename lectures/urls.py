from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='lectures'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
    
    path('add_to_cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    
    path('delete_from_cart/<int:cart_id>/', views.delete_from_cart, name='delete_from_cart'),
]