
from django.urls import path
from .views import *

urlpatterns = [
     
    # path('',product,name='product'),
    path('',HomePage.as_view(),name="home"),
    path("esewa-product-request/", EsewaProductRequestView.as_view(), name="esewarequest"),
    path("esewaproduct-verify/", EsewaProductVerifyView.as_view(), name="esewaverify"),
    path("khaltiproduct-request/", KhaltiProductRequestView.as_view(), name="khaltiproductrequest"),
    #this is the url for verifying whether khalti payment is success or not
    path("khaltiproduct-verify/", KhaltiProductVerifyView.as_view(), name="khaltiproductverify"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
