from django.shortcuts import render
from django.conf import settings

def home_view(request):
    return render(request, "home.html", {"restaurant_name": "Django Bites"})

def home_view2(request):
    return render(request, "home.html", {"phone": settings.RESTAURANT_PHONE})