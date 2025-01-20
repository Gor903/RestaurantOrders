import json
from datetime import datetime

from django.shortcuts import render
from django.views import View
from .forms import OrderForm
from .models import Order
from .choices import ORDER_STATUS


class OrderView(View):
    """
       Handles HTTP requests related to orders.

       This class provides views for managing orders, including listing orders,
       displaying order details, creating new orders, updating order statuses,
       and deleting orders.
    """

    def get(self, request, order_id=None):
        """
            Handles GET requests.

            - If `order_id` is provided, fetches and displays details of a specific order.
            - If `status` or `table_number` query parameters are present, filters orders by the specified criteria.
            - Otherwise, displays all orders.

            Args:
                request: The HTTP request object.
                order_id (int, optional): The ID of the order to retrieve. Defaults to None.

            Returns:
                HttpResponse: Rendered HTML response containing order details or a list of orders.
        """
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
        """
            Handles POST requests.

            Creates a new order using the submitted form data. If the form is valid,
            saves the new order to the database and then calls `get` to display the updated list of orders.

            Args:
                request: The HTTP request object.

            Returns:
                HttpResponse: Rendered HTML response with the updated list of orders.
        """
        order = OrderForm(request.POST)
        if order.is_valid():
            start = order.cleaned_data["start"]
            until = order.cleaned_data["until"]

            overlapping_order = Order.objects.filter(
                start__lt=until
            ).filter(
                until__gt=start,
            ).first()

            if overlapping_order:
                return self.get(
                    request=request,
                )
            order.save()
        return self.get(
            request=request,
        )

    def patch(self, request, order_id):
        """
            Handles PATCH requests.

            Updates the status of an existing order based on the provided `order_id` and request body.

            Args:
                request: The HTTP request object containing the new status in the body.
                order_id (int): The ID of the order to update.

            Returns:
                HttpResponse: Rendered HTML response displaying the updated order details.
        """
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
        """
            Handles DELETE requests.

            Deletes the specified order based on its order_id and then calls get
            to display the updated list of orders.

            Args:
                request: The HTTP request object.
                order_id (int): The ID of the order to delete.

            Returns:
                HttpResponse: Rendered HTML response with the updated list of orders.
        """
        order = Order.objects.filter(
            id=order_id,
        ).first()
        order.delete()
        return self.get(request=request)
