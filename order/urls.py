from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderView.as_view(), name="orders_all"),
    path("<uuid:order_id>/", views.OrderView.as_view(), name="order_detail"),
    path("delete/<uuid:order_id>/", views.OrderView.as_view(), name="delete_order"),
    path("update/<uuid:order_id>/", views.OrderView.as_view(), name="update_status"),
]
