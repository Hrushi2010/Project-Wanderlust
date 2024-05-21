import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def initiate_payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
    payment = client.order.create({'amount': 50000, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, 'payments/payment.html', {'payment': payment})

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        # handle success logic
        pass
    return render(request, 'payments/success.html')
