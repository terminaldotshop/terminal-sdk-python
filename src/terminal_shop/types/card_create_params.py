# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    token: Required[str]
    """Stripe card token.

    Learn how to [create one here](https://docs.stripe.com/api/tokens/create_card).
    """
