from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='login')
def my_reviews(request):
    reviews = Rating.objects.filter(student=request.user)
    
    context = {
        'reviews': reviews,
    }
    return render(request, 'students/my_reviews.html', context)

@login_required(login_url='login')
def give_review(request):
    if request.method == 'POST':
        form = RatingForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user
            review.rating = request.POST.get('rating')
            review.save()
            return redirect('my_reviews')
        
    else:
        form = RatingForm(user=request.user)
    return render(request, 'students/give_review.html', {'form': form})


