# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Subscription"]


class Subscription(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    address_id: str = FieldInfo(alias="addressID")
    """ID of the shipping address used for the subscription."""

    card_id: str = FieldInfo(alias="cardID")
    """ID of the card used for the subscription."""

    frequency: Literal["fixed", "daily", "weekly", "monthly", "yearly"]
    """Frequency of the subscription."""

    product_variant_id: str = FieldInfo(alias="productVariantID")
    """ID of the product variant being subscribed to."""

    quantity: int
    """Quantity of the subscription."""
