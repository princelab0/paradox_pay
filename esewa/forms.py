# from django import forms
# from django.conf import settings
# from django.utils.safestring import mark_safe
# # from paypal.standard.widgets import ValueHiddenInput, ReservedValueHiddenInput
# from esewa.conf import (POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT, RECEIVER_EMAIL)
# from esewa.conf import *
# class eSewaPaymentForm(forms.Form):
# 	'''
# 	tAmt 	= Amount of product/item required = True
# 	amt 	= Total amount of the product (includeing tax & service)  required = True
	
# 	txAmt 	= Tax amount on the product/item = false
# 	pdc 	= Delevery charge on product = false
# 	psc 	= Service charge  = false
	
# 	scd 	= Merchant/ service code provided by eSewa = true
# 	pid 	= A unique ID representing product/item  = True
# 	su 		= Sucess URI : a URI to redicet after sucessful transaction in esewa , True
# 	fu 		= Failure URI: a URI to redicet after failed transaction in eSewa , True

# 	'''
# 	tAmt = forms.IntegerField(widget=ValueHiddenInput())
# 	amt = forms.IntegerField(widget=ValueHiddenInput())
# 	txAmt = forms.IntegerField(widget=ValueHiddenInput())
# 	# txAmt = forms.CharField(widget=ValueHiddenInput())
# 	psc = forms.IntegerField(widget=ValueHiddenInput())
# 	pdc = forms.IntegerField(widget=ValueHiddenInput())
# 	scd = forms.CharField(widget=ValueHiddenInput())
# 	pid = forms.CharField(widget=ValueHiddenInput())
# 	su = forms.CharField(widget=ValueHiddenInput())
# 	fu = forms.CharField(widget=ValueHiddenInput())


# 	def __init__(self, button_type="buy", *args, **kwargs):
# 		super(eSewaPaymentForm, self).__init__(*args, **kwargs)
	 

# 	def render(self):
# 	    return mark_safe(u"""<form id="byitnow" action="%s" method="post"> %s
# 	        <div class="buyitnow"><input type="image" src="%s" border="0" name="submit" alt="Buy it Now" /></div>
# 			</form>""" % (POSTBACK_ENDPOINT, self.as_p(), self.get_image()))
            
# def sandbox(self):
# 	    return mark_safe(u"""<form action="%s" method="post"> %s 
# 	    	<input type="image" src="%s" border="0" name="submit" alt="Buy it Now" class="buyitnow"/>
# 			</form>""" % (SANDBOX_POSTBACK_ENDPOINT, self.as_p(), self.get_image()))
	 
# def get_image(self):
# 		return  IMAGE
