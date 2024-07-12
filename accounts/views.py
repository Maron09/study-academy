from django.shortcuts import render, redirect
from.forms import *
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from django.core.exceptions import PermissionDenied
from .utils import *
from teacher.models import *
from teacher.forms import *
from django.template.defaultfilters import slugify




def check_role_teacher(user):
    if user.role == 1:
        return True
    else:
        return PermissionDenied


def check_role_student(user):
    if user.role == 2:
        return True
    else:
        return PermissionDenied


def register_user(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Already registered')
        return redirect('my_account')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.STUDENT
            user.save()
            
            mail_subject = 'Activate your account'
            email_template = 'accounts/emails/account_activation_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            
            messages.success(request, "Registration successful -- Check your email for activation")
            return redirect('register_user')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def register_teacher(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Already Registered')
        return redirect('my_account')
    elif request.method == "POST":
        form = UserForm(request.POST)
        t_form = TeacherForm(request.POST, request.FILES)
        if form.is_valid() and t_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.TEACHER
            user.save()
            teacher = t_form.save(commit=False)
            teacher.user = user
            profession = t_form.cleaned_data['profession']
            teacher.teacher_slug = slugify(profession)+ '-' +str(user.id)
            user_profile = UserProfile.objects.get(user=user)
            teacher.user_profile = user_profile
            teacher.save()
            
            mail_subject = "Activate Your Account"
            email_template = 'accounts/emails/account_activation_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            
            messages.success(request, 'Registration Successful - Wait for Approval.')
            return redirect('register_teacher')
        else:
            print(form.errors)
    else:
        form = UserForm()
        t_form = TeacherForm()
    context = {
        'form': form,
        't_form': t_form,
    } 
    return render(request, 'accounts/register_teacher.html', context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid token')
        return redirect('my_account')

def login_page(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Already logged in')
        return redirect('my_account')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_page(request):
    auth.logout(request)
    messages.info(request, 'Logged out')
    return redirect('login')

@login_required(login_url='login')
def my_account(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
@user_passes_test(check_role_student)
def student_dashboard(request):
    return render(request, 'accounts/student_dashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_teacher)
def teacher_dashboard(request):
    return render(request, 'accounts/teacher_dashboard.html')