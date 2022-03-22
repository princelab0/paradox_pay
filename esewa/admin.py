from atexit import register
from django.contrib import admin
from .models import Product,Subscription,UserSubscription,Transaction,ActiveUSManager, eSewa,Github,Google,Facebook,Twitter

# Register your models here.

admin.site.register(Product)
admin.site.register(Subscription)
admin.site.register(UserSubscription)
admin.site.register(Transaction)
admin.site.register(eSewa)
admin.site.register(Github)
admin.site.register(Google)
admin.site.register(Facebook)
admin.site.register(Twitter)
# admin.site.register(ActiveUSManager)
 