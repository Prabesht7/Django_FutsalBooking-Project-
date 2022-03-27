from django.shortcuts import render
from django.views import View


class Userprofile(View):
    def get(self, request):
        return render(request, 'userprofile.html')
