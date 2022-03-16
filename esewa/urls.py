from django.urls import path
from .views import dashboard, homePage,EsewaRequestView,EsewaVerifyView,detail,subscription_list,subscription_detail
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # path('',homepage),
    path('',homePage.as_view(),name="home"),
    # path('<int:id>/esewa/',esewa,name="esewa"),
    # path('<int:pk>/esewa/',Esewa.as_view(),name="esewa"),
    #this is the url for request esewa payment
    path("esewa-request/<int:pk>/", EsewaRequestView.as_view(), name="esewarequest"),
    #this is the url for verifying whether esewa payment is success or not
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),

    #detail page
    path('detail/',detail,name="detail"),
    path('subscriptionlist/',subscription_list),
    path('cancel/', TemplateView.as_view(template_name='subscription/subscription_cancel.html'), name='subscription_cancel'),
    # path('subscriptiondetail/<object_id>',subscription_detail,name="subscription_detail"),
    path('subscription/<int:object_id>/subscription_detail/', subscription_detail.as_view(),name= 'subscription_detail'),
    path('dashboard/',dashboard,name="dashboard"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 