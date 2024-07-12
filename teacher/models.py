from django.db import models
from accounts.models import *
from accounts.utils import *




class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='userprofile')
    profession = models.CharField(max_length=100, blank=True, null=True)
    teacher_slug = models.SlugField(max_length=100, unique=True)
    certificate = models.ImageField(upload_to='teacher/certificate', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    @property
    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orign = Teacher.objects.get(pk=self.pk)
            if orign.is_approved != self.is_approved:
                mail_template = 'accounts/emails/admin_approval_email.html'
                context = {
                    'user': self.name,
                    'is_approved': self.is_approved,
                    'to_email': self.email,
                }
                if self.is_approved == True:
                    mail_subject = "Congratulations!!! You are now approved by Study Academy to Teach"
                    send_notification(mail_subject, mail_template, context)
                else:
                    mail_subject = "We're Sorry! You are not qualified to teach on Study Academy"
                    send_notification(mail_subject, mail_template, context)

