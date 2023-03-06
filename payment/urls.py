from django.urls import path
from .views import home, paypal_cancel, paypal_return

app_name = "payment"

urlpatterns = [

    path("", home, name='home'),
    path("paypal-return/", paypal_return, name='paypal-return'),
    path("paypal-cancel/", paypal_cancel, name='paypal-cancel'),

]