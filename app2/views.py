from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1>Virat is a Best Batsman</h1>')

def abd(request):
    return HttpResponse('<h1>ABD is MR360, He is a Monster</h1>')