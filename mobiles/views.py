from django.shortcuts import render

# Create your views here.
def search_in_mobiles(request):
    """searching in mobile warehouse"""
    return render(request,'mobiles.html')
    