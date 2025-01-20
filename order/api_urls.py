from django.urls import path
from . import api_views

urlpatterns = [
    path("", api_views.get_orders),
    path("create/", api_views.create_order),
    path("<uuid:id>/", api_views.get_order),
    path("update/<uuid:id>/", api_views.update_order),
    path("delete/<uuid:id>/", api_views.delete_order),
]
"""
URL patterns for order-related API endpoints.

Routes:
    - "" (GET): Retrieve a list of orders, optionally filtered by query parameters (`status`, `table_number`).
      Maps to `get_orders`.
    - "create/" (POST): Create a new order. Maps to `create_order`.
    - "<uuid:id>/" (GET): Retrieve a single order by its unique ID. Maps to `get_order`.
    - "update/<uuid:id>/" (PATCH): Update an existing order by its unique ID. Maps to `update_order`.
    - "delete/<uuid:id>/" (DELETE): Delete an order by its unique ID. Maps to `delete_order`.
"""
