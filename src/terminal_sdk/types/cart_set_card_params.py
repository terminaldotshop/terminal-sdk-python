# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CartSetCardParams"]


class CartSetCardParams(TypedDict, total=False):
    card_id: Required[Annotated[str, PropertyInfo(alias="cardID")]]
    """ID of the credit card to set for the current user's cart."""
