# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Profile", "User"]


class User(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    email: Optional[str] = None
    """Email address of the user."""

    fingerprint: Optional[str] = None
    """The user's fingerprint, derived from their public SSH key."""

    name: Optional[str] = None
    """Name of the user."""

    stripe_customer_id: str = FieldInfo(alias="stripeCustomerID")
    """Stripe customer ID of the user."""


class Profile(BaseModel):
    user: User
    """A Terminal shop user. (We have users, btw.)"""
