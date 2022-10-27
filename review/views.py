from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'review/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review_form.save()
            return redirect('review:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }

    return render(request, 'review/create.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review
    }
    return render(request, 'review/detail.html', context)

def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('review:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form
    }

    return render(request, 'review/update.html', context)

def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('review:index')