from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderView.as_view(), name="orders_all"),
    # Displays all orders or filters them based on query parameters
    # (`status` or `table_number`). Handles GET and POST requests
    # for the creation of new orders.
    path("<uuid:order_id>/", views.OrderView.as_view(), name="order_detail"),
    # Displays the details of a specific order identified by its UUID.
    # Handles GET requests for retrieving order details.
    path("delete/<uuid:order_id>/", views.OrderView.as_view(), name="delete_order"),
    # Deletes a specific order identified by its UUID.
    # Handles DELETE requests to remove an order from the database.
    path("update/<uuid:order_id>/", views.OrderView.as_view(), name="update_status"),
    # Updates the status of a specific order identified by its UUID.
    # Handles PATCH requests with the new status in the request body.
]
