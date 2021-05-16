from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('este es el index')


def home(request):
    
    return render(request,'Home.html')