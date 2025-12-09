# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Card", "Expiration"]


class Expiration(BaseModel):
    """Expiration of the card."""

    month: int
    """Expiration month of the card."""

    year: int
    """Expiration year of the card."""


class Card(BaseModel):
    """Credit card used for payments in the Terminal shop."""

    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    brand: str
    """Brand of the card."""

    created: str
    """Date the card was created."""

    expiration: Expiration
    """Expiration of the card."""

    last4: str
    """Last four digits of the card."""
