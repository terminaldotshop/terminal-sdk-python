# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .token import Token
from .._models import BaseModel

__all__ = ["TokenListResponse"]


class TokenListResponse(BaseModel):
    data: List[Token]
    """List of personal access tokens."""
