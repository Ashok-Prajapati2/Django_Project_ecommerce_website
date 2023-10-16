from django.contrib import admin
# from homeapp.models import category

# admin.site.register(category)

# class sadmin(admin.ModelAdmin):
#     list_display=('item_name','Price','item_img')
# admin.site.register(category.Fashion,sadmin)

# class elec(admin.ModelAdmin):
#     list_display=('item_name','Price','item_img')
# admin.site.register(category.ele,elec)


from homeapp.models import Fashion , ele

# admin.site.register(category)

class sadmin(admin.ModelAdmin):
    list_display=('item_name','Price','item_img')
admin.site.register(Fashion,sadmin)

class elec(admin.ModelAdmin):
    list_display=('item_name','Price','item_img')
admin.site.register(ele,elec)
