# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionUpdateParams", "Schedule", "ScheduleFixed", "ScheduleWeekly"]


class SubscriptionUpdateParams(TypedDict, total=False):
    address_id: Annotated[str, PropertyInfo(alias="addressID")]
    """New shipping address ID for the subscription."""

    card_id: Annotated[str, PropertyInfo(alias="cardID")]
    """New payment method ID for the subscription."""

    schedule: Schedule
    """New schedule for the subscription."""


class ScheduleFixed(TypedDict, total=False):
    type: Required[Literal["fixed"]]


class ScheduleWeekly(TypedDict, total=False):
    interval: Required[int]

    type: Required[Literal["weekly"]]


Schedule: TypeAlias = Union[ScheduleFixed, ScheduleWeekly]
