# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.product import Product

__all__ = ["ProductListResponse"]


class ProductListResponse(BaseModel):
    data: List[Product]
    """A list of products."""
