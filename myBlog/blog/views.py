from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'partial/home.html')

def single(request, id = None):
    return render(request, 'partial/single.html')
# Create your views here.
