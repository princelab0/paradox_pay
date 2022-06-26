from django.urls import path,include
# from .views import views
from app.views import Register,khaltirequest,logout,subscribe,Home,end_sub,subscribed,subscription,signin,index,check_mail_ajax, Login,EsewaVerifyView,KhaltiVerifyView,RegisterViewSet,LoginViewSet,UserViewSet,PayHistoryViewSet,UserMembershipViewSet,MembershipViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)
router.register(r'users', UserViewSet)
router.register(r'payhistory', PayHistoryViewSet)
router.register(r'usermembership', UserMembershipViewSet)
router.register(r'membership', MembershipViewSet)

urlpatterns = [
	path('', Home.as_view(), name='index'),
	path('login/', signin.as_view(), name='login'),
	path('home/', index, name='home'),
    path('logout/', logout, name='logout'),
    path('check-mail-ajax/',check_mail_ajax.as_view(), name='check_mail_ajax'),
    path('register/', Register.as_view(), name='register'),
    path('login-req', Login.as_view(), name='login_ajax'),
    path('esewa-verify/', EsewaVerifyView.as_view(), name="esewaverify"),
    path('subscription/', subscription.as_view(), name='subscription'),
    path('subscribe/', subscribe.as_view(), name='subscribe'),
    path('subscribed/',subscribed.as_view(), name='subscribed'),
    path('sub/', end_sub.as_view(), name='sub'),
    path("khalti-request/",khaltirequest.as_view(), name="khaltirequest"),
    #this is the url for verifying whether khalti payment is success or not
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path('api/', include(router.urls)),

]