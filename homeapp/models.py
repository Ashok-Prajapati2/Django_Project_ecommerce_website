
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
    
class Fashion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    item_img = models.ImageField(upload_to='homepage', max_length=100, null=True, default=None)

    def __str__(self):
        return self.item_name
 

