# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressCreateParams"]


class AddressCreateParams(TypedDict, total=False):
    city: Required[str]
    """City of the address."""

    country: Required[str]
    """ISO 3166-1 alpha-2 country code of the address."""

    name: Required[str]
    """The recipient's name."""

    street1: Required[str]
    """Street of the address."""

    zip: Required[str]
    """Zip code of the address."""

    phone: str
    """Phone number of the recipient."""

    province: str
    """Province or state of the address."""

    street2: str
    """Apartment, suite, etc. of the address."""
