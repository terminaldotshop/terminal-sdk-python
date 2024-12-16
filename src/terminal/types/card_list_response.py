# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .card import Card
from .._models import BaseModel

__all__ = ["CardListResponse"]


class CardListResponse(BaseModel):
    data: List[Card]
    """List of cards associated with the user."""
