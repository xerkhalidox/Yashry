from django.shortcuts import render


def test(request):
    return render(request, 'payment/payment_base.html')
