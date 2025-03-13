# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_variant import ProductVariant

__all__ = ["Product", "Tags"]


class Tags(BaseModel):
    app: Optional[str] = None

    color: Optional[str] = None

    featured: Optional[bool] = None

    market_eu: Optional[bool] = None

    market_na: Optional[bool] = None


class Product(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    description: str
    """Description of the product."""

    name: str
    """Name of the product."""

    variants: List[ProductVariant]
    """List of variants of the product."""

    order: Optional[int] = None
    """Order of the product used when displaying a sorted list of products."""

    subscription: Optional[Literal["allowed", "required"]] = None
    """Whether the product must be or can be subscribed to."""

    tags: Optional[Tags] = None
    """Tags for the product."""
