import json
from django.shortcuts import render
from django.views import View
from .forms import OrderForm
from .models import Order
from .choices import ORDER_STATUS


class OrderView(View):
    def get(self, request, order_id=None):
        if order_id:
            order = Order.objects.filter(
                id=order_id,
            ).first()
            return render(
                request=request,
                template_name="order_detail.html",
                context={"order": order, "order_status": [i[0] for i in ORDER_STATUS]},
            )
        else:
            if status := request.GET.get("status"):
                orders = Order.objects.filter(
                    status=status,
                ).all()
            elif table_number := request.GET.get("table_number"):
                orders = Order.objects.filter(
                    table_number=table_number,
                ).all()
            else:
                orders = Order.objects.all()
            form = OrderForm()
            return render(
                request=request,
                template_name="orders_all.html",
                context={
                    "orders": orders,
                    "form": form,
                    "order_status": [i[0] for i in ORDER_STATUS],
                },
            )

    def post(self, request):
        order = OrderForm(request.POST)
        if order.is_valid():
            order.save()
        return self.get(
            request=request,
        )

    def patch(self, request, order_id):
        data = json.loads(request.body)
        new_status = data.get("status")

        order = Order.objects.filter(id=order_id).first()

        order.status = new_status

        order.save()

        return render(
            request=request,
            template_name="order_detail.html",
            context={"order": order, "order_status": [i[0] for i in ORDER_STATUS]},
        )

    def delete(self, request, order_id):
        order = Order.objects.filter(
            id=order_id,
        ).first()
        order.delete()
        return self.get(request=request)
