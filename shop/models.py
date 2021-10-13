from django.db import models
from django.urls import reverse
# Create Model class for Category
# Fields are: category_name,slug,description and image

class Category(models.Model):
    #category_name and slug are unique
    category_name=models.CharField(max_length=150,unique=True) 
    slug=models.SlugField(max_length=150,unique=True) 
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    # create Meta class for Category
    class Meta:
        ordering=('category_name',)
        verbose_name="category"
        verbose_name_plural="categories"

    # create get_url function 
    def get_url(self):
        return reverse('shop:product_by_category',args=[self.slug])    
    # Display the category name in admin panel
    def __str__(self):
        return '{}'.format(self.category_name)

# Complete Category Model Class

#Create Model Class for Products
#Fields are:name,slug,description,price,category,image,stock,available,created,updated

class Product(models.Model):
    product_name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    image=models.ImageField(upload_to='products',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('shop:product_details',args=[self.category.slug,self.slug])

    # Create Meta Class
    class Meta:
        ordering=('product_name',)
        verbose_name='product'
        verbose_name_plural='products'

    # Display the category name in admin panel
    def __str__(self):
        return '{}'.format(self.product_name)











 





