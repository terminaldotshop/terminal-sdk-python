# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["Token", "Time"]


class Time(BaseModel):
    created: str
    """The created time for the token."""


class Token(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    token: str
    """Personal access token (obfuscated)."""

    time: Time
    """Relevant timestamps for the token."""
