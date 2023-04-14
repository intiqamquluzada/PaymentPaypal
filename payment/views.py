from django.shortcuts import render, redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.contrib import messages



def paypal_return(request):
    messages.success(request, "You paid successfully")
    return redirect("payment:home")


def paypal_cancel(request):
    messages.error(request, "Your paid didn't happen")
    return redirect("payment:home")


def home(request):

    host = request.get_host()
    print(host)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '20.00',
        "item_name": "Product 1",
        "invoice": str(uuid.uuid4()),
        "currency_code": "AZN",
        "notify_url": f"http://{host}{reverse('paypal-ipn')}",
        "return_url": f"http://{host}{reverse('payment:paypal-return')}",
        "cancel_url": f"http://{host}{reverse('payment:paypal-cancel')}",

    }
    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {
        "form": form,
    }
    return render(request, "home.html", context)


