from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from teacher.models import *
from courses.models import *
from .models import *
from orders.forms import *




def course_list(request):
    courses = Course.objects.select_related('teacher').all()
    context = {
        'courses': courses
    }
    return render(request, 'lectures/course_list.html', context)


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    # print(f"Retrieved course: {course}")
    sections = Section.objects.filter(course=course).prefetch_related('videos')
    # print(f"Retrieved sections: {sections}")
    section_data = []
    
    total_lessons = 0
    total_duration = 0
    for section in sections:
        videos = section.videos.all()
        section_total_duration = sum(video.get_duration() for video in videos)  # Ensure this line runs properly
        total_lessons += videos.count()
        total_duration += section_total_duration
        
        section_data.append({
            'section': section,
            'section_total_duration': section_total_duration,
            'videos': videos,
        })
        
        
        
    context = {
        'course': course,
        'sections': section_data,
        'total_lessons': total_lessons,
        'total_duration': total_duration,
    }
    return render(request, 'lectures/course_detail.html', context)


@login_required(login_url='login')
def cart_page(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    total_price = sum(item.course.price for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'lectures/cart.html', context)




def add_to_cart(request, course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, pk=course_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, course=course)
        
        
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
        
        total_price = sum(item.course.price for item in cart_items)
        item_details = [
            {
                'course': course.course_name,
                'price': course.price
            }
            for item in cart_items
        ]
        
        if created:
            message = 'Added to Cart'
        else:
            message = 'Already in Cart'
        print(f'Course ID: {course_id}, Message: {message}')
        return JsonResponse({
            'message': message,
            'total_price': total_price,
            'item_details': item_details,
            'cart_count': cart_count
        })
    message = 'Please Login to continue'
    return JsonResponse({'message': message})


def delete_from_cart(request, cart_id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user=request.user, pk=cart_id).first()
        if cart_item:
            cart_item.delete()
            
            cart_items = Cart.objects.filter(user=request.user)
            cart_count = cart_items.count()
            total_price = sum(item.course.price for item in cart_items)
            item_details = [
                {
                    'course': item.course.course_name,
                    'price': item.course.price
                }
                for item in cart_items
            ]
            message = 'Cart item deleted'
            return JsonResponse({
                'message': message,
                'total_price': total_price,
                'item_details': item_details,
                'cart_count': cart_count
            })
        return JsonResponse({
            'message': 'item does not exist'
        })
    return JsonResponse({
        'message': 'Login to Continue'
    })



@login_required(login_url='login')
def checkout_page(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    total_price = sum(item.course.price for item in cart_items)
    
    if cart_items.count() <= 0:
        return redirect('lectures')
    
    
    user_profile = UserProfile.objects.get(user=request.user)
    default_values = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'country': user_profile.country
    }
    form = OrderForm(initial=default_values)
    context = {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'lectures/checkout.html', context)