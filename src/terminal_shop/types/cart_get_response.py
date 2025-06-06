# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .cart import Cart
from .._models import BaseModel

__all__ = ["CartGetResponse"]


class CartGetResponse(BaseModel):
    data: Cart
    """The current Terminal shop user's cart."""
