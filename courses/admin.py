from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','teacher', 'modified_at')
    search_fields = ('category_name', 'teacher__user')
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'category', 'price', 'teacher', 'created_at', 'modified_at')
    search_fields = ('course_name', 'teacher__user')
    fieldsets = (
        (None, {
            'fields': ('course_name', 'description', 'category', 'intro_video', 'image', 'slug', 'price', 'teacher')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'modified_at')
        }),
    )
    readonly_fields = ('created_at', 'modified_at')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'course', 'order', 'created_at', 'modified_at')
    search_fields = ('section_title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'section', 'order')
    search_fields = ('video_title',)
