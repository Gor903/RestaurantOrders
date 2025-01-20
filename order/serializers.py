from rest_framework import serializers
from .models import Order, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        many=True,
    )

    class Meta:
        model = Order
        fields = [
            "table_number",
            "items",
        ]


class OrderSerializer(OrderCreateSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "table_number",
            "items",
            "status",
        ]

    def update(self, obj, validated_data):
        items = validated_data.pop("items", None)
        if items is not None:
            obj.items.set(items)

        for attr, value in validated_data.items():
            setattr(obj, attr, value)

        obj.save()
        return obj
