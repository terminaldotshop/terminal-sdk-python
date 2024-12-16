# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .shared.cart import Cart

__all__ = ["CartListResponse"]


class CartListResponse(BaseModel):
    data: Cart
    """The current Terminal shop user's cart."""
