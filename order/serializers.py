from rest_framework import serializers
from .models import Order, Item


class ItemSerializer(serializers.ModelSerializer):
    """
        Serializer for the Item model.

        Serializes the fields of the Item model to JSON format, including:
        - `title`: The name of the item.
        - `description`: A brief description of the item.
        - `price`: The price of the item.

        This serializer is used to represent items in the context of other serializers or API responses.
    """
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    """
        Serializer for creating orders.

        Handles the creation of new orders and includes:
        - `table_number`: The table number associated with the order.
        - `items`: A list of related Item instances, represented by their primary keys.

        The `items` field uses a PrimaryKeyRelatedField to enable linking existing items to the order.
    """

    items = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        many=True,
    )

    class Meta:
        model = Order
        fields = [
            "table_number",
            "items",
            "start",
            "until",
        ]


class OrderSerializer(OrderCreateSerializer):
    """
        Serializer for the Order model, including additional fields for retrieving or updating orders.

        Extends `OrderCreateSerializer` and adds:
        - `id`: The unique identifier for the order.
        - `status`: The current status of the order.

        Includes a custom `update` method to handle updates to the `items` relationship and other fields.
    """
    class Meta:
        model = Order
        fields = [
            "id",
            "table_number",
            "items",
            "status",
            "start",
            "until",
        ]

    def update(self, obj, validated_data):
        """
            Updates an existing order instance with validated data.

            If the `items` field is provided in `validated_data`, updates the associated items.
            Other fields are updated as provided.

            Args:
                obj: The existing order instance to update.
                validated_data: A dictionary of validated data to apply to the instance.

            Returns:
                Order: The updated order instance.
        """
        items = validated_data.pop("items", None)
        if items is not None:
            obj.items.set(items)

        for attr, value in validated_data.items():
            setattr(obj, attr, value)

        obj.save()
        return obj
