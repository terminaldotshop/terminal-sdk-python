# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .address import Address
from .._models import BaseModel

__all__ = ["AddressListResponse"]


class AddressListResponse(BaseModel):
    data: List[Address]
    """Shipping addresses."""
