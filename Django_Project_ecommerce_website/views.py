from django.shortcuts import render
from homeapp.models import Category , Fashion 
from django.core.paginator import Paginator

global_data = None

def paginator_function(data , show , request ):
    paginator = Paginator(data , show)
    page_num = request.GET.get('page')
    f_data = paginator.get_page(page_num)
    total_page = f_data.paginator.num_pages
    return { 'f_data': f_data , 'total_page' : total_page} 
    
def homepage(request):
    category_items = Category.objects.all().order_by('category_name')
    fashion_data_n = Fashion.objects.all().order_by('item_name')
    fashion_data = paginator_function(fashion_data_n, 3, request)
    total_page = fashion_data['total_page']
    fashion_data = fashion_data['f_data']
    
    data = {
         'fashion_data' : fashion_data , 'total_page' : total_page , 
          'category_items' : category_items ,
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
