# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.card import Card

__all__ = ["CardListResponse"]


class CardListResponse(BaseModel):
    data: List[Card]
    """List of cards associated with the user."""
