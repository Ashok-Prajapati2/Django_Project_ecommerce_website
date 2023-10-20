from django.contrib import admin
from .models import Category, Fashion 


class FashionAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price', 'item_img')
    list_filter = ('category',)  # Add filters if needed
    search_fields = ('item_name', 'category__category_name')  # Add search fields if needed

admin.site.register(Category)
admin.site.register(Fashion, FashionAdmin)  