from django import forms
from .models import *
from accounts.validators import *


class TeacherForm(forms.ModelForm):
    certificate = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images])
    profession = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-group'}))
    bio= forms.Textarea(attrs={'class': 'form-group'})
    class Meta:
        model = Teacher
        fields = ['bio', 'profession', 'certificate']
