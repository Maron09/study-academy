from django.db import models
from teacher.models import *


class Category(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='categories')
    category_name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    
    def clean(self):
        self.category_name = self.category_name.capitalize()
    
    
    def __str__(self):
        return self.category_name


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    course_name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    description = models.TextField()
    intro_video = models.FileField(upload_to='intro_video', blank=True, null=True)
    image = models.FileField(upload_to='course_images')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.course_name



class Section(models.Model):
    section_title = models.CharField(max_length=300)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.section_title



class Video(models.Model):
    video_title = models.CharField(max_length=300)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='section_videos')
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    
    def __str__(self):
        return self.video_title