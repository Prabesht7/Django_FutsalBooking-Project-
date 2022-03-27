from django.urls import path
from .views.contactus import contactus
from .views.homepage import firsthomepage
from .views.aboutus import aboutus


urlpatterns = [
    path('', firsthomepage, name='homepage'),
    path('aboutus', aboutus),
    path('contactus', contactus.as_view())
]
