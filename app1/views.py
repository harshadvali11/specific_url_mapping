from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1>MSD is a Best Finisher</h1>')

def raina(request):
    return HttpResponse('<h1> Raina is Known as MR.IPL</h1>')

