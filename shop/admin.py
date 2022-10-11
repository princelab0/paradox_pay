from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartProduct, Order, eSewa,Khalti
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
class OrderAdmin(admin.ModelAdmin):
    list_display=('cart','ordered_by','shipping_address','mobile','email','subtotal','discount','total','order_status','created_at','payment_method','payment_completed')
    list_filter = ('cart','ordered_by','total','payment_method','payment_completed')
    save_as = True
    save_on_top = True
    change_list_template=  'change_list_graph.html'
admin.site.register(Order)
admin.site.register(eSewa)
admin.site.register(Khalti)
