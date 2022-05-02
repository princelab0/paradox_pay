from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView   
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import CheckoutForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.urls import reverse
import requests

# Create your views here.

def product(request):
    return HttpResponse("hi there")


class HomePage(ListView):
    template_name = "shop/home.html"
    model = Product


class EsewaProductRequestView(View):
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
        esewa = eSewa.objects.get(id=1)
        context ={
            "order":order,
            'esewa':esewa
        }
        return render(request,"shop/esewarequest.html",context)


class EsewaProductVerifyView(View):
    def get(self, request, *args, **kwargs):

        import xml.etree.ElementTree as ET                  

        oid = request.GET.get("oid")                        
        amt = request.GET.get("amt")                        
        refId = request.GET.get("refId")                    

        url = "https://uat.esewa.com.np/epay/transrec"      

        d = {                                               
            'amt': amt,
            'scd': eSewa.objects.get(id=1).merchant_id,
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)                        

        root = ET.fromstring(resp.content)                                                 

        status = root[0].text.strip()                       

        order_id = oid 
         
        order_obj = Order.objects.get(id=order_id)

        if status == "Success":                             
            order_obj.payment_completed = True
            order_obj.save()
            return redirect("/")
        else:                                               
            return redirect("/esewaproduct-request/?o_id="+order_id)


def detail(request):
    return render(request,'detail.html')

class AddToCartView(TemplateView):
    template_name="shop/addtocart.html"

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
    template_name="shop/mycart.html"

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
    template_name="shop/checkout.html"
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
                return redirect(reverse("khaltiproductrequest") + "?o_id=" + str(order.id))
        else:
            return redirect("home")
        return super().form_valid(form)



class KhaltiProductRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        khalti = Khalti.objects.get(id=1)
        context = {
            "order": order,
            'khalti': khalti

        }
        return render(request, "shop/khaltirequest.html", context)


class KhaltiProductVerifyView(View):
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
            "Authorization": Khalti.objects.get(id=1).private_key,
        }

        order_obj = Order.objects.get(id=o_id)
        print(order_obj)
        response = requests.post(url, payload, headers=headers) 
        print(response)        
        resp_dict = response.json()  
        print(resp_dict)            

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