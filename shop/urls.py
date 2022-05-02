
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
     
    # path('',product,name='product'),
    path('',login_required(HomePage.as_view()),name="home"),
    path("esewa-product-request/", login_required(EsewaProductRequestView.as_view()), name="esewarequest"),
    path("esewaproduct-verify/", login_required(EsewaProductVerifyView.as_view()), name="esewaproductverify"),
    path("khaltiproduct-request/", login_required(KhaltiProductRequestView.as_view()), name="khaltiproductrequest"),
    #this is the url for verifying whether khalti payment is success or not
    path("khaltiproduct-verify/", login_required(KhaltiProductVerifyView.as_view()), name="khaltiproductverify"),
    path("add-to-cart-<int:pro_id>/", login_required(AddToCartView.as_view()), name="addtocart"),
    path("my-cart/", login_required(MyCartView.as_view()), name="mycart"),
    path("manage-cart/<int:cp_id>/", login_required(ManageCartView.as_view()), name="managecart"),
    path("empty-cart/", login_required(EmptyCartView.as_view()), name="emptycart"),
    path("checkout/", login_required(CheckoutView.as_view()), name="checkout"),
]
