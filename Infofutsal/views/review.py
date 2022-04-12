from django.shortcuts import render
from Infofutsal.models.review import Review
from django.contrib import messages
from django.views import View
from Shopping.models.customer import Customer


class review(View):
    def get(self, request):
        customer = Customer.get_all_customers();
        return render(request, 'review.html', {'customer': customer})

    def post(self, request):
        review = Review()
        fullname = request.POST.get('fullname')
        message = request.POST.get('message')
        photo = request.POST.get('photo')
        review.fullname = fullname
        review.message = message
        review.photo = photo
        review.save()
        messages.success(request, 'Your Review have been successfully added on About Us page!')
        return render(request, 'review.html')
