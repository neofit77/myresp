from django.http import HttpResponse
from django.shortcuts import render

my_dict = {'tekst_bre': 'tekst od templejta'}

def moja_funct(request):
    return HttpResponse('<h1>Proba</h1>')

def ren(request):
    return render(request, 'ulazna.html', my_dict)