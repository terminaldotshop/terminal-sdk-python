# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.card import Card
from .shared.cart import Cart
from .shared.user import User
from .shared.order import Order
from .shared.address import Address
from .shared.product import Product
from .shared.subscription import Subscription

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
