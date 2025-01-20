from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A form for creating and updating Order instances.

    This form is based on the `Order` model and provides fields for:
    - `table_number`: The table number associated with the order.
    - `items`: A list of items related to the order, displayed as a checkbox selection.

    Features:
        - Uses a `CheckboxSelectMultiple` widget for the `items` field to allow
          multiple selections.

    Meta:
        model: The model associated with this form (`Order`).
        fields: The fields included in the form (`table_number`, `items`).
        widgets: Customizes the display of the `items` field.
    """

    class Meta:
        model = Order
        fields = ["table_number", "items", "start", "until"]
        widgets = {
            "items": forms.CheckboxSelectMultiple(),
        }
