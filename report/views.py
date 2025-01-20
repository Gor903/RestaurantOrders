from django.http import JsonResponse
from django.shortcuts import render

from django.utils import timezone
from datetime import timedelta

from order.models import Order


def get_report(request):
    now = timezone.now()
    interval = int(request.GET.get("interval", 24))
    past = now - timedelta(hours=interval)

    orders = Order.objects.filter(start__gte=past)

    amount = sum([order.total_price for order in orders])

    data = {"orders": orders, "amount": amount}

    return render(
        request=request,
        template_name="report.html",
        context=data,
    )
