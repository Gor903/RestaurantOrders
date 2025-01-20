from django.urls import path
from . import api_views

urlpatterns = [
    path("", api_views.get_orders),
    path("create/", api_views.create_order),
    path("<uuid:id>/", api_views.get_order),
    path("update/<uuid:id>/", api_views.update_order),
    path("delete/<uuid:id>/", api_views.delete_order),
]
