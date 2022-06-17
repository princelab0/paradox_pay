from django.urls import path,include
from . import views
from .views import Register, Login,EsewaVerifyView,KhaltiVerifyView,RegisterViewSet,LoginViewSet,UserViewSet,PayHistoryViewSet,UserMembershipViewSet,MembershipViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)
router.register(r'users', UserViewSet)
router.register(r'payhistory', PayHistoryViewSet)
router.register(r'usermembership', UserMembershipViewSet)
router.register(r'membership', MembershipViewSet)

urlpatterns = [
	path('', views.home, name='index'),
	path('login/', views.signin, name='login'),
	path('home/', views.index, name='home'),
    path('logout/', views.logout, name='logout'),
    path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),
    path('register/', Register.as_view(), name='register'),
    path('login-req', Login.as_view(), name='login_ajax'),
    path('esewa-verify/', EsewaVerifyView.as_view(), name="esewaverify"),

    path('subscription/', views.subscription, name='subscription'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribed/', views.subscribed, name='subscribed'),
    path('sub/', views.end_sub, name='sub'),
    path("khalti-request/", views.khaltirequest, name="khaltirequest"),
    #this is the url for verifying whether khalti payment is success or not
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path('api/', include(router.urls)),

]