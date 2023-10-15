from django.contrib import admin
from homeapp.models import Fashion
class sadmin(admin.ModelAdmin):
    list_display=('item_name','Price','item_img')
admin.site.register(Fashion,sadmin)