# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Cart", "Amount", "Item", "Shipping"]


class Amount(BaseModel):
    subtotal: int
    """Subtotal of the current user's cart, in cents (USD)."""

    shipping: Optional[int] = None
    """Shipping amount of the current user's cart, in cents (USD)."""

    total: Optional[int] = None
    """Total amount after any discounts, in cents (USD)."""


class Item(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    product_variant_id: str = FieldInfo(alias="productVariantID")
    """ID of the product variant for this item in the current user's cart."""

    quantity: int
    """Quantity of the item in the current user's cart."""

    subtotal: int
    """Subtotal of the item in the current user's cart, in cents (USD)."""


class Shipping(BaseModel):
    service: Optional[str] = None
    """Shipping service name."""

    timeframe: Optional[str] = None
    """Shipping timeframe provided by the shipping carrier."""


class Cart(BaseModel):
    amount: Amount
    """The subtotal and shipping amounts for the current user's cart."""

    items: List[Item]
    """An array of items in the current user's cart."""

    subtotal: int
    """The subtotal of all items in the current user's cart, in cents (USD)."""

    address_id: Optional[str] = FieldInfo(alias="addressID", default=None)
    """ID of the shipping address selected on the current user's cart."""

    card_id: Optional[str] = FieldInfo(alias="cardID", default=None)
    """ID of the card selected on the current user's cart."""

    shipping: Optional[Shipping] = None
    """Shipping information for the current user's cart."""
