from django.http import  HttpResponseRedirect
from django.shortcuts import render
from homeapp.models import Fashion
from django.core.paginator import Paginator


def paginator_function(data , show , request ):
    paginator = Paginator(data , show)
    page_num = request.GET.get('page')
    f_data = paginator.get_page(page_num)
    total_page = f_data.paginator.num_pages
    return { 'f_data': f_data , 'total_page' : total_page}

def homepage(request):
    fashion_data_n = Fashion.objects.all().order_by('item_name')
    fashion_data = paginator_function(fashion_data_n, 3, request)
    total_page = fashion_data['total_page']
    fashion_data  = fashion_data['f_data']
    return render(request , 'homepage.html' , {'fashion_data' : fashion_data , 'total_page' : total_page})

def contact(request):
     return render(request , 'contact.html')
    
def electronic(request):
     return render(request , 'electronic.html')
    
def about(request):
     return render(request , 'about-us.html')
    
def prodectdetals(request):
     return render(request , 'prodectdetals.html')
    
def category(request):
     return render(request , 'category.html')
