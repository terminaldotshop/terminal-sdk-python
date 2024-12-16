# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .order import Order
from .._models import BaseModel

__all__ = ["OrderListResponse"]


class OrderListResponse(BaseModel):
    data: List[Order]
    """List of orders."""
