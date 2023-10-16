from django.db import models


# class category(models.Model):
#     category_name = models.CharField(max_length=20) 
    
class Fashion(models.Model):
    item_name = models.CharField(max_length=20)
    Price = models.CharField(max_length=5)
    item_img = models.FileField( upload_to='homepage', max_length=100,null= True , default=None)
    
class ele(models.Model):
    item_name = models.CharField(max_length=20)
    Price = models.CharField(max_length=5)
    item_img = models.FileField( upload_to='homepage', max_length=100,null= True , default=None)