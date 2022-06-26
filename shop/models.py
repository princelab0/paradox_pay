from django.db import models
from app.models import User
from django.db.models import Sum, Count, Max
from django.template.defaultfilters import date
import datetime


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

class Khalti(models.Model):
    public_key = models.CharField(max_length=150,blank=True,null=True)
    private_key = models.CharField(max_length=150,blank=True,null=True)
    
 

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
    MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}

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
        return "Order Id:" + str(self.id)+", " +"Order by "+str(self.ordered_by)+", "+"payment_completed: "+str(self.payment_completed)

    # @classmethod
    # def total_info(cls):
    #     return cls.objects.aggregate(total_sales=Sum('total'), total_orders=Count('id'), peek_sale=Max('total'))

    # @classmethod
    # def best_month(cls):
    #     res = {}
    #     month_price = cls.objects.values_list('created_at__month').annotate(total=Sum('total'))
    #     if month_price:
    #         res['month'], res['total'] = max(month_price, key=lambda i: i[1])
    #         res['month_name'] = date(datetime.date(datetime.datetime.now().year, month=res['month'], day=1), 'F')
    #     return res

    # @classmethod
    # def orders_month_report(cls):
    #     now = datetime.datetime.now()

    #     month_val = now.month + 1

    #     # Limit the upper value
    #     if month_val > 12:
    #         month_val = 12
        
    #     filter_params = {
    #         'created_at__date__gte': '{year}-{month}-{day}'.format(year=now.year - 1, month=month_val,
    #                                                                  day=now.day),
    #         'created_at__date__lte': now.date()
    #     }

    #     annotate_params = {
    #         'total_order': Count('id'),
    #         'total_price': Sum('total')
    #     }

    #     queryset = cls.objects.filter(**filter_params).values('created_at__year', 'created_at__month').annotate(**annotate_params)

    #     return list(queryset), [cls.MONTHS[data.get('created_at__month')] for data in queryset]



 
