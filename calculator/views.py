# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render , redirect
from calculator.forms import HomeForm


# Create your views here.
class HomePage(TemplateView):
    template_name = 'templatesviews/home.html'

    def get(self, request, *args, **kwargs):
        form = HomeForm()
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age_months']/12
            ht = form.cleaned_data['height_cm']
            wt = form.cleaned_data['weight_kg']
            amp = form.cleaned_data['amp_0_to_10']
            result = 0
            if 'female' in request.POST:
                a = (10*wt + 6.25*ht - 5*age - 161)*((amp/10)+1)
                result = str(a)
            elif 'male' in request.POST:
                a = (10*wt + 6.25*ht - 5*age + 5)*((amp/10)+1)
                result = str(a)
            if age<=1:
                result += '''Минералы:
Biotin (µg): 30-100
Calcium (mg): 1200
Phosphorus (mg): 1200
Magnesium (mg): 350
Iodine (µg): 150
Iron (mg): 18
Zinc (mg): 12-15
Copper (mg): 1,5-3
Selenium (µg): 50-70
Manganese (mg): 2,0-5,0
Chromium (µg): 50-200
Molybdenum (µg): 75-250
Витамины:
Vitamin A (IU): 5000
Vitamin B1 (mg): 1,5
Vitamin B2 (mg): 1,7
Niacin (mg): 20
Pantothenate (mg): 7-10
Vitamin B6 (mg): 2,0
Vitamin B12 (µg): 4,0-6,0
Vitamin C (mg): 60
Vitamin D (IU): 400
Vitamin E (IU): 15-30
Vitamin K (µg): 65-80'''
            else:
                result += '''
                1\n
                3\n
                4\n
                5\n
                '''

            form = HomeForm()
            #return redirect ('home:home')

        args = {'form': form , 'result': result}
        return render(request, self.template_name, args )


