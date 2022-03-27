from django.shortcuts import render
from django.http import HttpResponse
from Infofutsal.models import Contact
from django.contrib import messages

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')
