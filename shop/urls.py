
from django.urls.conf import include
from django.urls import path
from shop.views import CartProduct, KhaltiProductRequestView, KhaltiProductVerifyView,ProductViewSet,OrderViewSet,CartViewSet,HomePage,EsewaProductRequestView,EsewaProductVerifyView,KhaltiProductRequestView,KhaltiProductVerifyView, AddToCartView,MyCartView,ManageCartView,EmptyCartView,CheckoutView,get_filter_options,generate_color_palette,get_sales_chart,spend_per_customer_chart,payment_method_chart,payment_success_chart,statistics_view,payment,charge
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
     
    path('api',include(router.urls)),
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
    path('chart/filter-options/', get_filter_options, name='chart-filter-options'),
    path('chart/sales/<int:year>/', get_sales_chart, name='chart-sales'),
    path('chart/spend-per-customer/<int:year>/', spend_per_customer_chart, name='chart-spend-per-customer'),
    path('chart/payment-success/<int:year>/', payment_success_chart, name='chart-payment-success'),
    path('chart/payment-method/<int:year>/', payment_method_chart, name='chart-payment-method'),
    path('statistics/', statistics_view, name='shop-statistics'), 
    # this is for stripe payment
    path('payment/', payment.as_view(), name="payment"),
    path('charge/<int:o_id>/',charge,name='charge'),
]

