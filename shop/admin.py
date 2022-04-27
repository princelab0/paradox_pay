from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartProduct, Order, eSewa
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(eSewa)
