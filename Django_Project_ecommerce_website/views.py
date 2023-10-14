from django.http import  HttpResponseRedirect
from django.shortcuts import render


def homepage(request):
    return render(request , 'homepage.html')