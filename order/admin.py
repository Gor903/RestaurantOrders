from django.contrib import admin
from .models import Order, Item

admin.site.register(Order)
"""
The `Order` model is registered with the Django admin interface to allow 
administrators to manage orders. The `Order` model contains fields such as 
`table_number`, `status`, and `items`.
"""

admin.site.register(Item)
"""
The `Item` model is registered with the Django admin interface to allow 
administrators to manage individual items. The `Item` model contains fields 
such as `title`, `description`, and `price`.
"""
