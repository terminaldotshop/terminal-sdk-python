# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .card import Card
from .._models import BaseModel

__all__ = ["CardGetResponse"]


class CardGetResponse(BaseModel):
    data: Card
    """Credit card used for payments in the Terminal shop."""
