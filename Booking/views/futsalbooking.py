from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect


class futsalbooking(View):
    def get(self, request):
        print('you are: ', request.session.get('customer'))
        return render(request, 'futsalbooking.html')
