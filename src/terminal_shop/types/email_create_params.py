# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailCreateParams"]


class EmailCreateParams(TypedDict, total=False):
    email: Required[str]
    """Email address to subscribe to Terminal updates with."""
