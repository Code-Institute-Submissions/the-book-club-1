from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Review
from products.models import Book
from profiles.models import UserProfile

from .forms import ReviewForm


# Create your views here.
def reviews(request):
    """A view to return the reviews Community page"""
    reviews = Review.objects.all()

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


def write_review(request, book_id):
    """A view to allow a user to create a review"""

    book = get_object_or_404(Book, pk=book_id)
    print(book)
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            rating = form.cleaned_data['rating']
            print(rating)
            title = form.cleaned_data['title']
            print(title)
            review_text = form.cleaned_data['review_text']
            print(review_text)

            print(user)

            review = Review(book=book, user_profile=user, rating=rating, title=title,
                            review_text=review_text)
            review.save()
            messages.success(request, 'Your review was successfully posted on the Community page')

            return redirect(reverse('reviews'))

    else:
        form = ReviewForm()

        context = {
            'form': form,
            'book': book,
            'user': user,
        }

        template = 'reviews/write_review.html'

        return render(request, template, context)
