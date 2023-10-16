from django.http import  HttpResponseRedirect
from django.shortcuts import render
from homeapp.models import Fashion , ele
from django.core.paginator import Paginator


def paginator_function(data , show , request ):
    paginator = Paginator(data , show)
    page_num = request.GET.get('page')
    f_data = paginator.get_page(page_num)
    total_page = f_data.paginator.num_pages
    return { 'f_data': f_data , 'total_page' : total_page}

def homepage(request):
#     category_item =  category.objects.all().order_by('category_name')
#     print(category_item)
    fashion_data_n = Fashion.objects.all().order_by('item_name')
    electronic_data_n = ele.objects.all().order_by('item_name')
    
    fashion_data = paginator_function(fashion_data_n, 3, request)
    electronic_data = paginator_function(electronic_data_n, 3, request)
    
    total_page = fashion_data['total_page']
    e_total_page = electronic_data['total_page']
    
    fashion_data  = fashion_data['f_data']
    electronic_data = electronic_data['f_data']
    
    category = ['food' , 'toys']
    
    data = {
         'fashion_data' : fashion_data , 'total_page' : total_page , 
          'electronic_data' : electronic_data , 'e_total_page' : e_total_page , 
          
          'category' : category,
         
    }
    return render(request , 'homepage.html' , data)





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
