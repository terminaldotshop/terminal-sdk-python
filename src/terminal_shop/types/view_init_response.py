# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .app import App
from .card import Card
from .cart import Cart
from .order import Order
from .token import Token
from .region import Region
from .address import Address
from .product import Product
from .profile import Profile
from .._models import BaseModel
from .subscription import Subscription

__all__ = ["ViewInitResponse", "Data"]


class Data(BaseModel):
    addresses: List[Address]

    apps: List[App]

    cards: List[Card]

    cart: Cart
    """The current Terminal shop user's cart."""

    orders: List[Order]

    products: List[Product]

    profile: Profile
    """A Terminal shop user's profile. (We have users, btw.)"""

    region: Region
    """A Terminal shop user's region."""

    subscriptions: List[Subscription]

    tokens: List[Token]


class ViewInitResponse(BaseModel):
    data: Data
    """Initial app data."""
