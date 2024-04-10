from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class address(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='address')
    # customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    street=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=50,null=False,blank=False)
    state=models.CharField(max_length=50,null=False,blank=False)
    country=models.CharField(max_length=50,null=False,blank=False)
    zip_code=models.CharField(max_length=20,null=False,blank=False)

    # def __str__(self):
        # return self.user

class customer(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField(null=False,blank=False)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=200)
    # address=models.ForeignKey(address,on_delete=models.CASCADE)
    # address=models.TextField(help_text="must enter house-number street,city,zip-code and state,country")
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product')
    # seller=models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name

class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(product, related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cart=models.ForeignKey(cart,on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(address, on_delete=models.CASCADE, related_name='shipping_orders')
    order_status = models.CharField(max_length=50, default='pending',choices={
        ("pending","pending"),("done","done")
        })
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)