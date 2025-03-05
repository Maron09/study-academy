from django import forms
from .models import *
from accounts.validators import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class CourseForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images])
    intro_video = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_videos])
    class Meta:
        model = Course
        fields = ['category', 'course_name', 'description', 'for_who', 'reason', 'intro_video', 'image', 'price']



class SectionForm(forms.ModelForm):
    
    class Meta:
        model = Section
        fields = ['section_title', 'course', 'order']


class VideoForm(forms.ModelForm):
    video_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_videos])
    class Meta:
        model = Video
        fields = ['video_title', 'section', 'video_file', 'order']