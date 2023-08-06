from django.shortcuts import render, redirect
from django.db.models import Q,F
from django.views import View
from django.contrib import messages
from .models import Mobile
from .forms import MobileForm


class InsertMobile(View):
    """CBV for insering mobiles"""
    form_class = MobileForm
    template_class='insert_mobiles.html'
    def get(self, request):
        mobile_form = self.form_class()
        return render(request, self.template_class, {'mobile_form':mobile_form}) 
    
    def post(self, request):
        mobile_form = self.form_class(request.POST)
        if mobile_form.is_valid():
            new_mobile = mobile_form.save()
            messages.success(request, "New mobile was added to database",'success')
        
            return redirect('mobiles:insert_mobiles')
        
        return render(request, self.template_class, {'mobile_form':mobile_form})
    
    
    
def search_mobiles(request):
    return render(request,'search_mobiles.html')
def search_results(request):
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
                 
    return render(request, 'search_results.html',
                  {'brand': q_brand,'nationality': q_nationality, 'results': results})

    