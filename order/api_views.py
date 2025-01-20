from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import (
    OrderSerializer,
    OrderCreateSerializer,
)
from .choices import ORDER_STATUS

@swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            "status",
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=[i[0] for i in ORDER_STATUS],
            description="Filter orders by status (e.g., 'Pending', 'Ready', 'Paid').",
        ),
        openapi.Parameter(
            "table_number",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
            description="Filter orders by table number.",
        ),
    ],
    methods=["get"],
)
@api_view(["GET"])
def get_orders(request):
    """
    Retrieve a list of orders, optionally filtered by status or table number.

    Query Parameters:
        - `status` (str): Filter orders by their status.
        - `table_number` (int): Filter orders by their table number.

    Returns:
        Response: A JSON array of orders matching the filters, serialized using the `OrderSerializer`.
    """
    orders = Order.objects.all()
    if status := request.query_params.get("status"):
        orders = orders.filter(status=status)
    if table_number := request.query_params.get("table_number"):
        orders = orders.filter(table_number=table_number)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_order(request, id):
    """
    Retrieve the details of a single order by its ID.

    Parameters:
        - `id` (UUID): The unique identifier of the order.

    Returns:
        Response: A JSON object containing the order details, serialized using the `OrderSerializer`.
                  Returns a 404 status if the order is not found.
    """
    order = Order.objects.filter(id=id).first()
    if not order:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@swagger_auto_schema(
    operation_description="Create a new order.",
    request_body=OrderCreateSerializer,
    methods=["post"],
)
@api_view(["POST"])
def create_order(request):
    """
    Create a new order.

    Request Body:
        - A JSON object containing the required fields for an order, validated by `OrderCreateSerializer`.

    Returns:
        Response: A JSON object of the created order with a 201 status on success.
                  Returns a 400 status if validation fails.
    """
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@swagger_auto_schema(
    operation_description="Update an order.",
    request_body=OrderSerializer,
    methods=["patch"],
)
@api_view(["PATCH"])
def update_order(request, id):
    """
    Update an existing order by its ID.

    Parameters:
        - `id` (UUID): The unique identifier of the order.

    Request Body:
        - A JSON object containing the fields to update, validated by `OrderSerializer`.

    Returns:
        Response: A JSON object of the updated order with a 201 status on success.
                  Returns a 404 status if the order is not found or a 400 status if validation fails.
    """
    order = Order.objects.filter(id=id).first()
    if not order:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(
        order,
        data=request.data,
        partial=True,
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["DELETE"])
def delete_order(request, id):
    """
    Delete an order by its ID.

    Parameters:
        - `id` (UUID): The unique identifier of the order.

    Returns:
        Response: A success message if the order is deleted successfully.
                  Returns a 404 status if the order is not found.
    """
    order = Order.objects.filter(id=id).first()
    if not order:
        return Response(status=status.HTTP_404_NOT_FOUND)

    order.delete()
    return Response(
        {
            "message": "Order deleted successfully!",
        },
    )
