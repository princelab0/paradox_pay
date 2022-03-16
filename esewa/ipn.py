# '''
# 	esewa ipn manual configuration
# 	update order table 
# 	save order conformation details

# 	Note: catch django signals and update your order table
# '''

# from urllib.parse import urljoin

# import datetime
# from django.conf import settings

# def esewaIpnValidate(request):
# 	from esewa.models import eSewa
# 	if request.method == 'GET' and request.META.__contains__('HTTP_REFERER'):
# 		referer = request.META['HTTP_REFERER']
# 		url = request.get_full_path()
		
# 		rp = urljoin(referer)
# 		up = urljoin(url)
# 		if rp.netloc == paymentUrl and rp.path=='/epay/confirmation':
# 			# payment conformation details
# 			# payment sucess
# 			# conform order
# 			# oid=262&amt=1476.06&refId=0008LGK#destinations

# 			if request.GET.__contains__('oid') and request.GET.__contains__('amt') and request.GET.__contains__('refId'):
# 				e = eSewa(
# 					order_id=request.GET['oid'],
# 					refId = request.GET['refId'],
# 					amount = request.GET['amt'],
# 					date = datetime.datetime.now(),
# 					)
# 				try:
# 					e.save()
# 				except:
# 					pass
			
# 		if rp.netloc == 'dev.esewa.com.np' and rp.path =='/home':
# 			# payment unsucess
# 			# cancle the payment system 
# 			# set pending order

# 			# print 'Pending order'
# 			pass