from django.contrib import admin
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'profession', 'is_approved', 'created_at')
    list_display_links = ('user',)
    list_editable = ('is_approved',)
    search_fields = ('user__first_name', 'user__last_name', 'profession')
    list_filter = ('is_approved', 'created_at')



admin.site.register(Teacher, TeacherAdmin)