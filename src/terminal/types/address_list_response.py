# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.address import Address

__all__ = ["AddressListResponse"]


class AddressListResponse(BaseModel):
    data: List[Address]
    """Shipping addresses."""
