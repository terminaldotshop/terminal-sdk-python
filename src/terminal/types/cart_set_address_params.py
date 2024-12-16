# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CartSetAddressParams"]


class CartSetAddressParams(TypedDict, total=False):
    address_id: Required[Annotated[str, PropertyInfo(alias="addressID")]]
    """ID of the shipping address to set for the current user's cart."""
