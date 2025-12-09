from django.db import models
import uuid

# Create your models here.
class Basemodels(models.Model):
    uid  = models.UUIDField(default= uuid.uuid4, editable= False, primary_key= True)
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_created= True)

    class Meta:# iske through humari ye models ki class  class kintaraha treats hogi na ki models ki  
        abstract = True 

      
class Product(Basemodels):
    Product_name = models.CharField(max_length= 100)
    product_slug = models.SlugField(unique= True)
    product_description = models.TextField()
    product_price  = models.IntegerField(default= 0 )
    product_demo_price  = models.IntegerField(default= 0)
  
   
   
                                         
    

class Productmetainformation(Basemodels):
    product = models.OneToOneField(Product , on_delete= models.CASCADE)
    product_quantity = models.CharField(null= True, blank=True)
    product_measuring = models.CharField(max_length= 100, choices=(("KG","KG"),("ML", "ML"), ("L","L"),(None,None)))
    is_restricted = models.BooleanField(default=False)
    restricted_quantity = models.IntegerField() 
     
     

class ProductImage(Basemodels):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= "image")
        product_image =  models.ImageField(upload_to= "product")
       

class Dummymodel(models.Model):
    pass

      


    