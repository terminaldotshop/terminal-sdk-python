# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .product import Product
from .._models import BaseModel

__all__ = ["ProductListResponse"]


class ProductListResponse(BaseModel):
    data: List[Product]
    """A list of products."""
