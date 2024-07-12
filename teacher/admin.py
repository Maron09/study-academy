from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession','is_approved', 'created_at')
    list_display_links = ('user',)
    list_editable = ('is_approved',)



admin.site.register(Teacher, TeacherAdmin)