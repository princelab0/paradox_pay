from django.db import models
from app.models import User

# Create your models here.

# Product model
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products",null=True,blank=True)
    description = models.TextField(max_length=300,null=True,blank=True)
    price = models.IntegerField()
    # payment_completed = models.BooleanField(default=False, null=True, blank=True)

# this is for the display the title in the admin panel
    def __str__(self):
        return self.title




class eSewa(models.Model):
	 merchant_id = models.CharField(max_length=100,default='epay_payment')
    
 

class Cart(models.Model):
    customer= models.OneToOneField(User, on_delete= models.SET_NULL,null=True, blank= True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return "Cart:" + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=0)
    product= models.ForeignKey(Product, on_delete= models.CASCADE)
    rate = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    subtotal = models.PositiveBigIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + "CartProduct:" + str(self.id)

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
("Cash On Delivery","Cash On Delivery"),
("Esewa","Esewa"),
("Khalti", "Khalti"),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank= True)
    subtotal = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField()
    total = models.PositiveBigIntegerField()
    order_status = models.CharField(max_length=50, choices= ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add= True)
    payment_method = models.CharField(max_length=20,choices=METHOD,default="Cash On Delivery")
    payment_completed = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return "Order:" + str(self.id)
 
