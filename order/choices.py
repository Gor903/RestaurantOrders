ORDER_STATUS = (
    ("Pending", "Pending"),
    ("Ready", "Ready"),
    ("Paid", "Paid"),
)
"""
Defines the possible statuses for an order.

Each status is represented as a tuple:
    - The first value is the internal value stored in the database.
    - The second value is the human-readable display name.

Statuses:
    - "Pending": The order is not yet ready.
    - "Ready": The order is prepared and ready to be served.
    - "Paid": The order has been paid for.
"""
