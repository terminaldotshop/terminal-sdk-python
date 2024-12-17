# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .app import App
from .._models import BaseModel

__all__ = ["AppListResponse"]


class AppListResponse(BaseModel):
    data: List[App]
    """List of apps."""
