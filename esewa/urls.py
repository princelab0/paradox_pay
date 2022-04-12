from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # path('',homepage),
    path('',HomePage.as_view(),name="home"),
    # path('<int:id>/esewa/',esewa,name="esewa"),
    # path('<int:pk>/esewa/',Esewa.as_view(),name="esewa"),
    #this is the url for request esewa payment
    path('register/',register, name='register'),
    # path("esewa-request/<int:id>/", EsewaRequestView.as_view(), name="esewarequest"),
    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    #this is the url for verifying whether esewa payment is success or not
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    #this is the url for verifying whether khalti payment is success or not
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),

    #detail page
    path('detail/',detail,name="detail"),
    path('subscriptionlist/',subscription_list),
    path('cancel/', TemplateView.as_view(template_name='subscription/subscription_cancel.html'), name='subscription_cancel'),
    # path('subscriptiondetail/<object_id>',subscription_detail,name="subscription_detail"),
    path('subscription/<int:object_id>/subscription_detail/', subscription_detail.as_view(),name= 'subscription_detail'),
    path('dashboard/',dashboard,name="dashboard"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 