from django import forms
from .models import *



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['course', 'rating', 'review']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RatingForm, self).__init__(*args, **kwargs)
        if user:
            enrolled_courses = Course.objects.filter(enrollments__student=user)
            self.fields['course'].queryset = enrolled_courses
        self.fields['rating'].widget = forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)])