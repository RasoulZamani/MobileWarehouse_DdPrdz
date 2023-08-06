from django.shortcuts import render
from .models import Mobile
from django.db.models import Q,F


def search_in_mobiles(request):
    """searching in mobile warehouse"""
    if request.method == "GET":
        q_nationality = request.GET.get('nationality')
        q_brand = request.GET.get('brand')
        q_CountryEqNational = request.GET.get('CountryEqNational')
        if q_brand == '':
            q_brand = 'None'
        if q_nationality == '':
            q_nationality = 'None'

        results = Mobile.objects.filter(
            Q(nationality__icontains=q_nationality)  | Q(brand__icontains=q_brand) 
            )
        
        if q_CountryEqNational == 'Yes':
            results = results.filter(nationality__icontains=F('country'))
            print(q_brand)
            if q_brand=='None' and q_nationality=='None':
                results = Mobile.objects.filter(nationality__icontains=F('country'))
                 
    return render(request, 'mobiles.html',
                  {'brand': q_brand,'nationality': q_nationality, 'results': results})

    