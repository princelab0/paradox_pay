from itertools import product
from unicodedata import name
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView   
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product
import requests 
from django.contrib.sites.models import Site
from .models import Subscription, UserSubscription,eSewa,Order,Cart,CartProduct
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CheckoutForm
from django.urls import reverse_lazy
from django.http import JsonResponse

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
        # order = get_object_or_404(Product, id=kwargs['pk'])
        # context = {
        #     "order":order
        # }
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id= o_id)
        print(order)
        context ={
            "order":order
        }
        return render(request,"esewarequest.html",context)


# http://127.0.0.1:8000/esewa-verify/?oid=2&amt=150.0&refId=0002YFQ

#EsewaVerifyView where we verify whether payment is success/verified or not.

# class EsewaVerifyView(View):
#     def get(self, request, *args, **kwargs):

#         # here we use xml to show the tree structure
#         import xml.etree.ElementTree as ET     
#         #here we fetch the data from url             
#         oid = request.GET.get("oid")                        
#         amt = request.GET.get("amt")                        
#         refId = request.GET.get("refId")     
#         print(oid,amt,refId)               

#         url = "https://uat.esewa.com.np/epay/transrec"  
           

#         d = {                                               
#             'amt': amt,
#             'scd': eSewa.objects.get(id=1) ,   
#             'rid': refId,
#             'pid': oid,

#             # 'amt': 100,
#             # 'scd': 'EPAYTEST',
#             # 'rid': '000AE01',
#             # 'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d453',
#         }
#         resp = requests.post(url, d)  

#         #this is the xml syntax for showing the message in string format
#         root = ET.fromstring(resp.content)   
#         print(root[0].text)                                              
#         status = root[0].text.strip() 
#         print(status)      
#         order_id = oid                                 
#         # order_obj = Product.objects.get(id=id)
#         try:
#             order_obj = Order.objects.get(id = order_id)
#             print(order_obj)
#             if status == "Success":
#                 print(status)
#                 order_obj.payment_completed = True
#                 order_obj.save()
#                 return redirect("/")
#             else:
#                 print("failed")
#                 return redirect("/esewa-request/?o_id="+order_id)
#         except:
#             order_obj = Subscription.objects.get(id = order_id)
#             #here we check whether success or not
           
#             if status == "Success":  
#                 print(status)     
#                 order_obj.payment_completed = True
#                 order_obj.save()                     
#                 return redirect("/dashboard")
#             else:                                               
#                         #return redirect("/esewa/?p_id="+order_obj)
#                 return redirect("/esewa-request/?o_id="+order_id)


class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):

        import xml.etree.ElementTree as ET                  

        oid = request.GET.get("oid")                        
        amt = request.GET.get("amt")                        
        refId = request.GET.get("refId")                    

        url = "https://uat.esewa.com.np/epay/transrec"      

        d = {                                               
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)                        

        root = ET.fromstring(resp.content)                                                 

        status = root[0].text.strip()                       

        order_id = oid 
        try:

            order_obj = Order.objects.get(id=order_id)

            if status == "Success":                             
                order_obj.payment_completed = True
                order_obj.save()
                return redirect("/")
            else:                                               
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
        return render(request,"subscription/esewarequest.html",context)



    


 

# @method_decorator(login_required,name='dispatch')
def dashboard(request):
    sub = Subscription.objects.filter(payment_completed=True) 
    for i in sub:
        if i.name=="Basic":
            return render(request,"subscription/dashboard.html",{"sub":sub})
        else:

            return render(request,"subscription/dashboard1.html",{'sub':sub})

from .forms import  UserRegistrationForm
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'registration/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/register.html',{'user_form': user_form})


class AddToCartView(TemplateView):
    template_name="addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        # get product id from requested url
        product_id = self.kwargs['pro_id']
        
        #get product
        product_obj = Product.objects.get(id=product_id)
        #check whether cart exists
        cart_id = self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj= Cart.objects.get(id= cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
            #where items already exist in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.price
                cartproduct.save()
                cart_obj.total += product_obj.price
                cart_obj.save()
            else:
                # new items added in cart
                cartproduct= CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.price, quantity=1, subtotal=product_obj.price)
                cart_obj.total += product_obj.price
                cart_obj.save()
        else:
            cart_obj=Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(cart= cart_obj, product=product_obj, rate=product_obj.price, quantity= 1, subtotal=product_obj.price)
            cart_obj.total += product_obj.price
            cart_obj.save()
        #check if product already exists in cart

        return context


class EmptyCartView (View):
    def get(self, request, *args, **kwargs ):
        cart_id = request.session.get("cart_id",None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("mycart")


class MyCartView(TemplateView):
    template_name="mycart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id=self.request.session.get("cart_id", None)
        if cart_id:
            cart=Cart.objects.get(id=cart_id)
        else:
            cart=None
        
        context['cart']=cart
        return context 

class ManageCartView(View):
    def get(self, request, *args, **kwargs):
        
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart
        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity ==0 :
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        return redirect("mycart")

class CheckoutView(CreateView):
    template_name="checkout.html"
    form_class= CheckoutForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id  = self.request.session.get("cart_id",None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context
    def form_valid(self, form):
        cart_id= self.request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.discount = 0 
            form.instance.total = cart_obj.total
            form.instance.order_status = "Order Received"
            del self.request.session['cart_id']
            pm = form.cleaned_data.get("payment_method")
            order = form.save()
            if pm == "Esewa":
                return redirect(reverse("esewarequest")+ "?o_id=" + str(order.id))
            elif pm == "Khalti":                              
                return redirect(reverse("khaltirequest") + "?o_id=" + str(order.id))
        else:
            return redirect("home")
        return super().form_valid(form)



class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, "khaltirequest.html", context)


class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")                    
        amount = request.GET.get("amount")                  
        o_id = request.GET.get("order_id")                  

        url = "https://khalti.com/api/v2/payment/verify/"   

        payload = {                                 
            "token": token,
            "amount": amount
        }

        headers = {                                
            "Authorization": "Key <your_secret_key>"
        }

        order_obj = Order.objects.get(id=o_id)
        print(order_obj)
        response = requests.post(url, payload, headers=headers) 
        print(response)        
        resp_dict = response.json()               

        if resp_dict.get("idx"):                 
            success = True                        
            order_obj.payment_completed = True    
            order_obj.save()                      

        else:                                     
            success = False                         

        data = {
            "success": success
        }

        return JsonResponse(data)          
     




    