# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProductVariant", "Tags"]


class Tags(BaseModel):
    app: Optional[str] = None

    market_eu: Optional[bool] = None

    market_global: Optional[bool] = None

    market_na: Optional[bool] = None


class ProductVariant(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    name: str
    """Name of the product variant."""

    price: int
    """Price of the product variant in cents (USD)."""

    tags: Optional[Tags] = None
    """Tags for the product variant."""
