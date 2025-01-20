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
        ),
        openapi.Parameter(
            "table_number",
            openapi.IN_QUERY,
            type=openapi.TYPE_INTEGER,
        ),
    ],
    methods=["get"],
)
@api_view(["GET"])
def get_orders(request):
    orders = Order.objects.all()
    if status := request.query_params.get("status"):
        orders = orders.filter(status=status)
    if table_number := request.query_params.get("table_number"):
        orders = orders.filter(table_number=table_number)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_order(request, id):
    order = Order.objects.filter(id=id).first()
    if not order:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@swagger_auto_schema(
    operation_description="Create a new order",
    request_body=OrderCreateSerializer,
    methods=["post"],
)
@api_view(["POST"])
def create_order(request):
    serializer = OrderCreateSerializer(
        data=request.data,
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


@swagger_auto_schema(
    operation_description="Update an order",
    request_body=OrderSerializer,
    methods=["patch"],
)
@api_view(["PATCH"])
def update_order(request, id):
    order = Order.objects.filter(
        id=id,
    ).first()
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
    order = Order.objects.filter(id=id).first()
    if not order:
        return Response(status=status.HTTP_404_NOT_FOUND)

    order.delete()
    return Response(
        {
            "message": "Order deleted successfully!",
        },
    )
