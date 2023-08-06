from django.shortcuts import render

# Create your views here.
def home(request):
    """home page for mobile shop"""
    return render(request, 'home.html')