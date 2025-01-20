from django.core.validators import MinValueValidator
from django.db import models
import uuid
from .choices import ORDER_STATUS


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class Order(BaseModel):
    table_number = models.IntegerField(
        validators=[MinValueValidator(1)],
        unique=True,
        null=False,
    )
    items = models.ManyToManyField(
        to="Item",
        null=False,
    )
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        null=False,
        blank=False,
        default="Pending",
    )

    @property
    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"{self.table_number} - {self.status}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Item(BaseModel):
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=[MinValueValidator(0)],
        null=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
