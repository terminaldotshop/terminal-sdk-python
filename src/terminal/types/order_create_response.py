# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .shared.order import Order

__all__ = ["OrderCreateResponse"]


class OrderCreateResponse(BaseModel):
    data: Order
    """An order from the Terminal shop."""