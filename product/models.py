from django.db import models
import uuid

# Create your models here.
class Basemodels(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    # use DateTimeField with auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

      
class Product(Basemodels):
    Product_name = models.CharField(max_length= 100)
    product_slug = models.SlugField(unique= True)
    product_description = models.TextField()
    product_price  = models.IntegerField(default= 0 )
    product_demo_price  = models.IntegerField(default= 0)
    def __str__(self) -> str:
         return self.Product_name

  

   
   
                                         
    

class Productmetainformation(Basemodels):
    product = models.OneToOneField(Product , on_delete= models.CASCADE)
    product_quantity = models.CharField(null= True, blank=True)
    MEASURING_CHOICES = (
        ("KG", "KG"),
        ("ML", "ML"),
        ("L", "L"),
    )
    product_measuring = models.CharField(max_length= 10, choices=MEASURING_CHOICES, null=True, blank=True)
    is_restricted = models.BooleanField(default=False)
    restricted_quantity = models.IntegerField(default=0)
   


    
     

class ProductImage(Basemodels):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= "image")
        product_image =  models.ImageField(upload_to= "product")
       

class Dummymodel(models.Model):
    pass

      


    