# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .product_variant import ProductVariant

__all__ = ["Product"]


class Product(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    description: str
    """Description of the product."""

    filters: List[Literal["eu", "na"]]

    name: str
    """Name of the product."""

    variants: List[ProductVariant]
    """List of variants of the product."""

    order: Optional[int] = None
    """Order of the product used when displaying a sorted list of products."""

    subscription: Optional[Literal["allowed", "required"]] = None
    """Whether the product must be or can be subscribed to."""

    tags: Optional[Dict[str, str]] = None
    """Tags for the product."""
