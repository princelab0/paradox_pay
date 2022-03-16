from atexit import register
from django.contrib import admin
from .models import Product,Subscription,UserSubscription,Transaction,ActiveUSManager, eSewa

# Register your models here.

admin.site.register(Product)
admin.site.register(Subscription)
admin.site.register(UserSubscription)
admin.site.register(Transaction)
admin.site.register(eSewa)
# admin.site.register(ActiveUSManager)
 