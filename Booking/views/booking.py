from django.shortcuts import render, redirect, HttpResponseRedirect
from Booking.models.booking import Booking
from Booking.forms import AddBooking
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from Shopping.models.customer import Customer
from django.views import View


class FutsalBooking(View):
    model = Booking
    template_name = 'booking.html'

    def get(self, request):
        print('you are: ', request.session.get('email'))
        return render(request, "booking.html")

    def post(self, request, ):
        postData = request.POST
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer')
        booking_date = request.POST.get('booking_date')
        date = request.POST.get('date')
        time = request.POST.get('time')
        template = render_to_string('email_template.html', {'fullname': fullname, 'date': date, 'time': time})
        send_mail(
            'Futsal Booked Sucessfully!',
            template,
            'Brihaspatifutsal2018@gmail.com',
            [email],
            fail_silently=False,
        )
        playing_hours = request.POST.get('playing_hours')
        value = {
            'fullname': fullname,
            'email': email,
            'phone': phone,
            'address': address,
            'date': date,
            'booking_date': booking_date,
            'time': time,
            'playing_hours': playing_hours
        }

        error_message = None
        booking = Booking(fullname=fullname,
                          phone=phone,
                          address=address,
                          date=date,
                          time=time,
                          playing_hours=playing_hours)
        error_message = self.validateBooking(booking)
        if not error_message:
            print(fullname, phone, address, date, time , customer)
            booking.save()
            return redirect('send-mail')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'booking.html', data)

    def validateBooking(self, booking):
        error_message = None
        if (not booking.fullname):
            error_message = "Full Name Required!"
        elif len(booking.fullname) < 4:
            error_message = "Full Name must be 4 char long or more."
        elif not booking.address:
            error_message = "Address Required"
        elif len(booking.address) < 4:
            error_message = "Address must be 4 char long or more."
        elif not booking.phone:
            error_message = "Phone Number Required."
        elif len(booking.phone) < 10:
            error_message = "Phone Number must be 10 char long."
        elif booking.phoneisExists():
            error_message = "Phone Number is already registered."
        elif booking.timeisExists():
            error_message = "Futsal is Booked at this Time."
        return error_message


def all_booking(request):
    booking_list = Booking.objects.all()
    return render(request, 'booked.html', {'booking_list': booking_list})


def add_booking(request):
    if request.method == 'POST':
        fm = AddBooking(request.POST)
        if fm.is_valid():
            fullname = fm.cleaned_data['fullname']
            phone = fm.cleaned_data['phone']
            address = fm.cleaned_data['address']
            date = fm.cleaned_data['date']
            time = fm.cleaned_data['time']
            playing_hours = fm.cleaned_data['playing_hours']
            reg = Booking(fullname=fullname, phone=phone, address=address, date=date, time=time,
                          playing_hours=playing_hours)
            reg.save()
            fm = AddBooking()
            return redirect('bookings')
    else:
        fm = AddBooking()
    return render(request, 'add_booking.html', {'form': fm})


def delete_booking(request, id):
    if request.method == 'POST':
        db = Booking.objects.get(pk=id)
        db.delete()
        return HttpResponseRedirect('/bookings')


def update_booking(request, id):
    if request.method == 'POST':
        pi = Booking.objects.get(pk=id)
        fm = AddBooking(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('bookings')
        else:
            pi = Booking.objects.get(pk=id)
            fm = AddBooking(instance=pi)
    else:
        pi = Booking.objects.get(pk=id)
        fm = AddBooking(instance=pi)
    return render(request, 'update_booking.html', {'form': fm})


def sendmail(request):
    send_mail(
        'Futsal Time have been Booked!',
        'Hi , This is a mail to confirm that new Futsal Time have been booked.',
        'Brihaspatifutsal2018@gmail.com',
        ['numb1prabesht7@gmail.com'],
        fail_silently=False,
    )
    return redirect('bookings')
