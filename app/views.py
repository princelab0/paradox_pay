from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import *
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, MembershipSerializer, PayHistorySerializer, UserMembershipSerializer
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import datetime
import requests
import stripe
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from.models import User
from shop.models import Khalti, eSewa
from rest_framework.viewsets import ModelViewSet
from django.views.generic import View, TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
today = datetime.date.today()




class RegisterViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer

class LoginViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = LoginSerializer

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PayHistoryViewSet(ModelViewSet):
	queryset = PayHistory.objects.all()
	serializer_class = PayHistorySerializer

class UserMembershipViewSet(ModelViewSet):
	queryset = UserMembership.objects.all()
	serializer_class = UserMembershipSerializer

class MembershipViewSet(ModelViewSet):
	queryset = Membership.objects.all()
	serializer_class = MembershipSerializer


 
# def home(request):
# 	if request.user.is_authenticated:
# 		return redirect('home/')
# 	else:
# 		return render(request, 'index.html')

class Home(TemplateView):
	template_name = 'index.html'
	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home/')
		# else:
		# 	return render (request,'index.html')
		return super().dispatch(request, *args, **kwargs)
 

def index(request):
	user_membership = UserMembership.objects.get(user=request.user)
	print(user_membership)
	subscriptions = Subscription.objects.filter(user_membership=user_membership).exists()
	if subscriptions == False:
		return redirect('sub')
	else:
		subscription = Subscription.objects.filter(user_membership=user_membership).last()
		return render(request, 'home.html', {'sub': subscription})
	

# def signin(request):	
# 	if request.user.is_authenticated:
# 		return redirect('/')
# 	else:
# 		return render(request, 'login.html')

class signin(TemplateView):
	template_name = 'login.html'
	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		return super().dispatch(request, *args, **kwargs)


# def check_mail_ajax(request):
# 	if request.is_ajax():
# 		email = request.GET.get('email', None)
# 		check_email = User.objects.filter(email=email).exists()
# 		if check_email == True:
# 			response = {'error': 'Email already exists.'}
# 			return JsonResponse(response)
# 		else:
# 			response = {'success': 'Cool'}
# 			return JsonResponse(response)
# 	else:
# 		response = {'error': 'Error Email Checking.'}
# 		return JsonResponse(response)

class check_mail_ajax(View):
	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			email = request.GET.get('email', None)
			check_email = User.objects.filter(email=email).exists()
			if check_email == True:
				response = {'error': 'Email already exists.'}
				return JsonResponse(response)
			else:
				response = {'success': 'Cool'}
				return JsonResponse(response)
		else:
			response = {'error': 'Error Email Checking.'}
			return JsonResponse(response)


class Register(APIView):
	def post(self, request):
		serializer = RegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			obj = serializer.save()
			password = make_password(serializer.data['password'])
			User.objects.filter(email=serializer.data['email']).update(password=password)
			get_membership = Membership.objects.get(membership_type='Free')
			instance = UserMembership.objects.create(user=obj, membership=get_membership)
			return Response({'success': 'Registration successful.'})

		else:
			return Response({'error': 'Error. Try again'})


class Login(APIView):
	def post(self, request):
		email = request.data.get('email')
		password = request.data.get('password')

		# Let us check if the user exists or not...
		check_email = User.objects.filter(email=email).exists()
		if check_email == False:
			return Response({'error': 'No account with such email'})
		# We need to check if the user password is correct
		user = User.objects.get(email=email)
		if user.check_password(password) == False:
			return Response({'error': 'Password is not correct. Try again'})
		# Now let us log the user in
		log_user = auth.authenticate(email=email, password=password)
		if user is not None:
			auth.login(request, log_user)
			return Response({'success': 'Login successful'})
		else:
			return Response({'error': 'Invalid email/password. Try again later.'})


# def subscription(request):
# 	return render(request, 'subscription.html')

class subscription(TemplateView):
	template_name= 'subscription.html'

# def end_sub(request):
# 	return render(request, 'sub.html')

class end_sub(TemplateView):
	template_name='sub.html'


 

# def subscribe(request):
# 	plan = request.GET.get('sub_plan')
# 	fetch_membership = Membership.objects.filter(membership_type=plan).exists()
# 	if fetch_membership == False:
# 		return redirect('subscribe')
# 	membership = Membership.objects.get(membership_type=plan)
# 	price = float(membership.price)  
# 	amount = int(price)
	
# 	instance = PayHistory.objects.create(amount= amount, payment_for=membership, user=request.user)
# 	esewa_id = eSewa.objects.get(id=1)
	
# 	context = {
# 		'instance': instance,
# 		'esewa_id':esewa_id
# 	}
# 	UserMembership.objects.filter(user=instance.user).update(membership=membership)
# 	return render(request, 'esewarequest.html',context)


class subscribe(View):
	def get(self,request,*args,**kwargs):
		plan = request.GET.get('sub_plan')
		fetch_membership = Membership.objects.filter(membership_type=plan).exists()
		if fetch_membership == False:
			return redirect('subscribe')
		membership = Membership.objects.get(membership_type=plan)
		price = float(membership.price)  
		amount = int(price)

		instance = PayHistory.objects.create(amount= amount, payment_for=membership, user=request.user)
		esewa_id = eSewa.objects.get(id=1)

		context = {
			'instance': instance,
			'esewa_id':esewa_id
		}
		UserMembership.objects.filter(user=instance.user).update(membership=membership)
		return render(request, 'esewarequest.html',context)


class EsewaVerifyView(View):
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
        order_obj = PayHistory.objects.get(id=order_id)

        if status == "Success":                             
            order_obj.paid = True
            order_obj.save()
            return redirect("/")
        else:                                               
            return redirect("/subscribe/?o_id="+order_id)
                

# def subscribed(request):
# 	return render(request, 'subscribed.html')

class subscribed(TemplateView):
	template_name = 'subscribed.html'


# def  khaltirequest(request):   
# 	plan = request.GET.get('sub_plan')
# 	fetch_membership = Membership.objects.filter(membership_type=plan).exists()
# 	if fetch_membership == False:
# 		return redirect('subscribe')
# 	membership = Membership.objects.get(membership_type=plan)
# 	price = float(membership.price)  
# 	amount = int(price)
# 	instance = PayHistory.objects.create(amount= amount, payment_for=membership, user=request.user)
# 	khalti = Khalti.objects.get(id=1)
# 	context = {
# 		'instance': instance,
# 		'khalti':khalti
# 	}
# 	UserMembership.objects.filter(user=instance.user).update(membership=membership)
# 	return render(request,"khaltirequest.html", context)

class khaltirequest(View):
	def get(self,request,*args,**kwargs):
		plan = request.GET.get('sub_plan')
		fetch_membership = Membership.objects.filter(membership_type=plan).exists()
		if fetch_membership == False:
			return redirect('subscribe')
		membership = Membership.objects.get(membership_type=plan)
		price = float(membership.price)  
		amount = int(price)
		instance = PayHistory.objects.create(amount= amount, payment_for=membership, user=request.user)
		khalti = Khalti.objects.get(id=1)
		context = {
		'instance': instance,
		'khalti':khalti
		}
		UserMembership.objects.filter(user=instance.user).update(membership=membership)
		return render(request,"khaltirequest.html", context)



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
            "Authorization":  Khalti.objects.get(id=1).private_key,
        }
		
        order_obj = PayHistory.objects.get(id=o_id)
        print(order_obj)
        response = requests.post(url, payload, headers=headers) 
        print(response)   
		     
        resp_dict = response.json()               
        if resp_dict.get("idx"):                 
            success = True                        
            order_obj.paid = True    
            order_obj.save()                      

        else:                                     
            success = False                         

        data = {
            "success": success
        }

        return JsonResponse(data)   

class Subpayment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/payment.html'

    def get(self, request, *args, **kwargs):
        key = "your publishable key"
        plan = request.GET.get("sub_plan")
        fetch_membership = Membership.objects.filter(membership_type=plan).exists()
        if fetch_membership == False:
            return redirect('subscribe')
        membership = Membership.objects.get(membership_type=plan)
        price = membership.price 
        amount = price
        instance = PayHistory.objects.create(amount= amount, payment_for=membership, user=request.user)
        price = amount*100;
        total = round(amount,2)
        if request.method == 'POST':
            charge = stripe.Charge.create(amount=total,
                currency='usd',
                description=name,
                source=request.POST['stripeToken'])
        UserMembership.objects.filter(user=instance.user).update(membership=membership)
        return Response( {"key": key, "total": total,"instance":instance})
         

def charge(request,o_id):
	# order = Order.objects.get(user=request.user, ordered=False)
    # print(abc)
    order_obj = PayHistory.objects.get(id=o_id) 

    order_total = order_obj.amount               
    totalCents = int(order_total * 100)
    print(totalCents)
    stripe.api_key= "your secret key"
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=totalCents,
            currency='usd',
            description= order_obj,
            source=request.POST['stripeToken'])
        print('abc')
            
        if charge.status == "succeeded":
            # orderId = get_random_string(length=16, allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            print(charge.id)
            order_obj.paid = True    
            order_obj.save() 
            # order.paymentId = charge.id
            # order.orderId = f'#{request.user}{orderId}'
            # order.save()
            # cartItems = Cart.objects.filter(user=request.user)
            # for item in cartItems:
            #     item.purchased = True
            #     item.save()
            return render(request, 'users/charge.html')



 

def logout(request):
	auth.logout(request)
	return redirect('/')

 