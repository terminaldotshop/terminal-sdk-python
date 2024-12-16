# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionListResponse"]


class SubscriptionListResponse(BaseModel):
    data: List[Subscription]
    """List of subscriptions."""
