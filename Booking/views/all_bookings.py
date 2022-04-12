from django.shortcuts import render, redirect, HttpResponseRedirect
from Booking.models.booking import Booking
from Booking.forms import AddBooking
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from Shopping.models.customer import Customer
from django.views import View


class all_booking(View):
    def get(self, request):
        customer = request.session.get('customer')
        booking_list = Booking.get_bookings_by_customer(customer)
        print(booking_list)
        return render(request, 'booked.html', {'booking_list': booking_list})

    def post(self, request):
        return render(request, 'orders.html')
