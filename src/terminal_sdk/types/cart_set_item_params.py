# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CartSetItemParams"]


class CartSetItemParams(TypedDict, total=False):
    product_variant_id: Required[Annotated[str, PropertyInfo(alias="productVariantID")]]
    """ID of the product variant to add to the cart."""

    quantity: Required[int]
    """Quantity of the item to add to the cart."""
