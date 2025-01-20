from django.test import TestCase
from .models import Item, Order


class OrderTestCase(TestCase):
    """
    Test case for the Order model.

    This class includes tests to ensure that the Order model behaves as expected.
    It tests the order creation, total price calculation, and string representation.
    """

    def setUp(self):
        """
        Set up the initial data for the test cases.

        This method creates two `Item` instances and associates them with an `Order`.
        The order is created with a table number of 1, and both items are added to the order.
        """
        self.item1 = Item.objects.create(title="BBQ", description="Tasty meat", price=10.3)
        self.item2 = Item.objects.create(title="Juices", description="Fanta, Sprite", price=5.5)

        self.order = Order.objects.create(table_number=6)
        self.order.items.set([self.item1, self.item2])

    def test_order_creation(self):
        """
        Test that an order is created correctly with the correct fields.

        This test checks that an order with table number 1 has:
        - a default status of "Pending"
        - the correct table number
        - the correct number of associated items.
        """
        order = Order.objects.get(table_number=6)
        self.assertEqual(order.status, "Pending")
        self.assertEqual(order.table_number, 6)
        self.assertEqual(order.items.count(), 2)

    def test_order_total_price(self):
        """
        Test the total price calculation for an order.

        This test verifies that the total price of the order is calculated correctly,
        which should be the sum of the prices of all items in the order.
        """
        total_price = self.order.total_price
        self.assertEqual(total_price, 15.8)

    def test_order_string_representation(self):
        """
        Test the string representation of an order.

        This test ensures that the string representation of the order returns the expected format,
        which is "<table_number> - <status>".
        """
        self.assertEqual(str(self.order), "6 - Pending")
