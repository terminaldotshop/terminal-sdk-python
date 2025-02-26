# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderCreateParams"]


class OrderCreateParams(TypedDict, total=False):
    address_id: Required[Annotated[str, PropertyInfo(alias="addressID")]]
    """Shipping address ID."""

    card_id: Required[Annotated[str, PropertyInfo(alias="cardID")]]
    """Card ID."""

    variants: Required[Dict[str, int]]
    """Product variants to include in the order, along with their quantities."""
