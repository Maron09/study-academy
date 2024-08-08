from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from lectures.models import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from .utils import *





@login_required(login_url='login')
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    total_price = sum(item.course.price for item in cart_items)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('lectures')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.email = form.cleaned_data['email']
            order.country = form.cleaned_data['country']
            order.user = request.user
            order.total_amount = total_price
            order.save()
            order.order_number = generate_order_number(order.id)
            order.save()
            context = {
                'order': order,
                'cart_items': cart_items,
                'total_price': total_price
            }
            return render(request, 'orders/place_order.html', context)
        else:
            print(form.errors)
    return render(request, 'orders/place_order.html')



@login_required(login_url='login')
def payments(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and 'POST':
        order_number = request.POST.get('order_number')
        payment_id = request.POST.get('payment_id')
        status = request.POST.get('payment_id')
        
        
        order = Order.objects.get(user=request.user, order_number=order_number)
        payment = Payment(
            user = request.user,
            payment_id = payment_id,
            amount = order.total_amount,
            status = status
        )
        payment.save()
        
        order.payment = payment
        order.save()
        
        
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            
            order_item = OrderItem()
            order_item.order = order
            order_item.course = item.course
            order_item.price = item.price
            order_item.save()
            
        
        
        # cart_items.delete()
        response = {
            'order_number': order_number,
            'payment_id': payment_id
        }
        return JsonResponse(response)
    return HttpResponse('Payment view')