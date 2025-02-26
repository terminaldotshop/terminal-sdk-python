# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Subscription", "Schedule", "ScheduleFixed", "ScheduleWeekly"]


class ScheduleFixed(BaseModel):
    type: Literal["fixed"]


class ScheduleWeekly(BaseModel):
    interval: int

    type: Literal["weekly"]


Schedule: TypeAlias = Union[ScheduleFixed, ScheduleWeekly]


class Subscription(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    address_id: str = FieldInfo(alias="addressID")
    """ID of the shipping address used for the subscription."""

    card_id: str = FieldInfo(alias="cardID")
    """ID of the card used for the subscription."""

    product_variant_id: str = FieldInfo(alias="productVariantID")
    """ID of the product variant being subscribed to."""

    quantity: int
    """Quantity of the subscription."""

    next: Optional[str] = None
    """Next shipment and billing date for the subscription."""

    schedule: Optional[Schedule] = None
    """Schedule of the subscription."""
