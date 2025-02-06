# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    id: Required[str]
    """Unique object identifier. The format and length of IDs may change over time."""

    address_id: Required[Annotated[str, PropertyInfo(alias="addressID")]]
    """ID of the shipping address used for the subscription."""

    card_id: Required[Annotated[str, PropertyInfo(alias="cardID")]]
    """ID of the card used for the subscription."""

    frequency: Required[Literal["fixed", "daily", "weekly", "monthly", "yearly"]]
    """Frequency of the subscription."""

    product_variant_id: Required[Annotated[str, PropertyInfo(alias="productVariantID")]]
    """ID of the product variant being subscribed to."""

    quantity: Required[int]
    """Quantity of the subscription."""

    next: str
    """Next shipment and billing date for the subscription."""
