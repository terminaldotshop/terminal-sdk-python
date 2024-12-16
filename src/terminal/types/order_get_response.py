# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .order import Order
from .._models import BaseModel

__all__ = ["OrderGetResponse"]


class OrderGetResponse(BaseModel):
    data: Order
    """An order from the Terminal shop."""
