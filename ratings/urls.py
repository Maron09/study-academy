from django.urls import path
from . import views


urlpatterns = [
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('submit-review/', views.give_review, name='submit_review'),
]