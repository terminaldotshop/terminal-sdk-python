# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .card import Card
from .cart import Cart
from .user import User
from .order import Order
from .address import Address
from .product import Product
from .._models import BaseModel
from .subscription import Subscription

__all__ = ["UserInitResponse", "Data"]


class Data(BaseModel):
    addresses: List[Address]

    cards: List[Card]

    cart: Cart
    """The current Terminal shop user's cart."""

    orders: List[Order]

    products: List[Product]

    subscriptions: List[Subscription]

    user: User
    """A Terminal shop user. (We have users, btw.)"""


class UserInitResponse(BaseModel):
    data: Data
    """Initial app data."""
