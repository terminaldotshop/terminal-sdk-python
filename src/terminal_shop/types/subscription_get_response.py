# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionGetResponse"]


class SubscriptionGetResponse(BaseModel):
    data: Subscription
    """Subscription to a Terminal shop product."""
