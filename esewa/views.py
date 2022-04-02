from itertools import product
from unicodedata import name
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView   
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product
import requests 
from django.contrib.sites.models import Site
from .models import Subscription, UserSubscription,eSewa
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# from esewa.providers import PaymentMethodFactory
from django.http import Http404

# Create your views here.


#this is function based homepage view

# def homepage(request):
#     pro = Product.objects.all()
#     return render(request,'home.html',{"pro":pro})


#fucnction based esewa request view
# def esewa(request,id):
#     prod = get_object_or_404(Product,id=id)
#     return render(request,'esewa.html',{"prod":prod})



#homgePage view where we list all of the product
# @method_decorator(login_required,name='dispatch')
class HomePage(ListView):
    template_name = "home.html"
    model = Product



#EsewaRequstView where we request for the payment of product to the esewa payment gateway
# @method_decorator(login_required,name='dispatch')


class EsewaRequestView(View):
    def get(self,request,*args,**kwargs):
        # o_id = request.GET.get(kwargs['pk'])
        # print(o_id)
        # order = Product.objects.get(pk=o_id)
        order = get_object_or_404(Product, id=kwargs['pk'])
        context = {
            "order":order
        }
        return render(request,"esewarequest.html",context)


# http://127.0.0.1:8000/esewa-verify/?oid=2&amt=150.0&refId=0002YFQ

#EsewaVerifyView where we verify whether payment is success/verified or not.

class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):

        # here we use xml to show the tree structure
        import xml.etree.ElementTree as ET     
        #here we fetch the data from url             
        oid = request.GET.get("oid")                        
        amt = request.GET.get("amt")                        
        refId = request.GET.get("refId")     
        print(oid,amt,refId)               

        url = "https://uat.esewa.com.np/epay/transrec"  
           

        d = {                                               
            'amt': amt,
            'scd': eSewa.objects.get(id=1) ,   
            'rid': refId,
            'pid': oid,

            # 'amt': 100,
            # 'scd': 'EPAYTEST',
            # 'rid': '000AE01',
            # 'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
        }
        resp = requests.post(url, d)  

        #this is the xml syntax for showing the message in string format
        root = ET.fromstring(resp.content)   
        print(root[0].text)                                              
        status = root[0].text.strip() 
        print(status)      
        order_id = oid                                 
        # order_obj = Product.objects.get(id=id)
        try:
            order_prod = Product.objects.get(id = order_id)
            print(order_prod)
            if status == "Success":
                print(status)
                order_prod.payment_completed = True
                order_prod.save()
                return redirect("/")
            else:
                print("failed")
                return redirect("/esewa-request/?o_id="+order_id)
        except:
            order_obj = Subscription.objects.get(id = order_id)
            #here we check whether success or not
           
            if status == "Success":  
                print(status)     
                order_obj.payment_completed = True
                order_obj.save()                     
                return redirect("/dashboard")
            else:                                               
                        #return redirect("/esewa/?p_id="+order_obj)
                return redirect("/esewa-request/?o_id="+order_id)




def detail(request):
    return render(request,'detail.html')



 

# this is the subscription list view where we will list all the objects or subscription plan
# @method_decorator(login_required,name='dispatch')
def subscription_list(request):
    # here first of all we will list all the objects
    object_list=Subscription.objects.all() 
    # here we use for loop to iterate tha object_list
    for i in object_list:
        print(i.name)
        print(i.payment_completed)
        # here we filter the objects whose payment is completed
        if i.payment_completed == True:
            # if already paid we will redirect to dashboard
            return redirect("/dashboard")

        # if payment is not completed we will show the subscription plan to the user
        else:
            return render(request, 'subscription/subscription_list.html',{"object_list":object_list})
    
     

     
    # object_list = Subscription.objects.filter(name=name)
     
            

     
    




# this is the subscription detail plan where we will redirect the subscription plan for the payment purpose
# @method_decorator(login_required,name='dispatch')
class subscription_detail(View):
    def get(self,request,*args,**kwargs):
        # o_id = request.GET.get(kwargs['pk'])
        # print(o_id)
        # order = Product.objects.get(pk=o_id)
        order = get_object_or_404(Subscription, id=kwargs['object_id'])
        context = {
            "order":order
        }
        return render(request,"esewarequest.html",context)



    


 

# @method_decorator(login_required,name='dispatch')
def dashboard(request):
    sub = Subscription.objects.filter(payment_completed=True) 
    for i in sub:
        if i.name=="Basic":
            return render(request,"subscription/dashboard.html",{"sub":sub})
        else:

            return render(request,"subscription/dashboard1.html",{'sub':sub})


    