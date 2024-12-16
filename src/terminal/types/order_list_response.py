# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.order import Order

__all__ = ["OrderListResponse"]


class OrderListResponse(BaseModel):
    data: List[Order]
    """List of orders."""
