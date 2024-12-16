# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Order", "Amount", "Item", "Shipping", "Tracking"]


class Amount(BaseModel):
    shipping: int
    """Shipping amount of the order, in cents (USD)."""

    subtotal: int
    """Subtotal amount of the order, in cents (USD)."""


class Item(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    amount: int
    """Amount of the item in the order, in cents (USD)."""

    quantity: int
    """Quantity of the item in the order."""

    description: Optional[str] = None
    """Description of the item in the order."""

    product_variant_id: Optional[str] = FieldInfo(alias="productVariantID", default=None)
    """ID of the product variant of the item in the order."""


class Shipping(BaseModel):
    city: str
    """City of the address."""

    country: str
    """ISO 3166-1 alpha-2 country code of the address."""

    name: str
    """The recipient's name."""

    street1: str
    """Street of the address."""

    zip: str
    """Zip code of the address."""

    phone: Optional[str] = None
    """Phone number of the recipient."""

    province: Optional[str] = None
    """Province or state of the address."""

    street2: Optional[str] = None
    """Apartment, suite, etc. of the address."""


class Tracking(BaseModel):
    number: Optional[str] = None
    """Tracking number of the order."""

    service: Optional[str] = None
    """Shipping service of the order."""

    url: Optional[str] = None
    """Tracking URL of the order."""


class Order(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    amount: Amount
    """The subtotal and shipping amounts of the order."""

    items: List[Item]
    """Items in the order."""

    shipping: Shipping
    """Shipping address of the order."""

    tracking: Tracking
    """Tracking information of the order."""

    index: Optional[int] = None
    """Zero-based index of the order for this user only."""
