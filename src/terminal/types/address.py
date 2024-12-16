# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    city: str
    """City of the address."""

    country: str
    """ISO 3166-1 alpha-2 country code of the address."""

    name: str
    """The recipient's name."""

    street1: str
    """Street of the address."""

    zip: str
    """Zip code of the address."""

    phone: Optional[str] = None
    """Phone number of the recipient."""

    province: Optional[str] = None
    """Province or state of the address."""

    street2: Optional[str] = None
    """Apartment, suite, etc. of the address."""
