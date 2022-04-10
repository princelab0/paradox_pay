from atexit import register
from django.contrib import admin
from .models import Cart, CartProduct, Order, Product,Subscription,UserSubscription,Transaction,ActiveUSManager, eSewa,Github,Google,Facebook,Twitter

# Register your models here.

admin.site.register(Product)
admin.site.register(Subscription)
admin.site.register(UserSubscription)
admin.site.register(Transaction)
admin.site.register(eSewa)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartProduct)
# admin.site.register(Customer)
# admin.site.register(ActiveUSManager)
 