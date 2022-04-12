from django.shortcuts import render, redirect
from django.views import View
from Shopping.models.customer import Customer
from Shopping.forms import UserUpdateForm
from django.contrib import messages
from Shopping.forms import updateprofile


class Userprofile(View):
    def get(self, request):
        customer = Customer.get_all_customers();
        print(customer)
        return render(request, 'userprofile.html', {'customer': customer})


def update_profile(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    form = updateprofile(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('userprofile')
    customer = Customer.objects.get(pk=customer_id)
    form = updateprofile(request.POST or None, instance=customer)
    return render(request, 'updateprofile.html', {'customer': customer, 'form': form})
