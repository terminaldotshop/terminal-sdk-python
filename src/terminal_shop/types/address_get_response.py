# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .address import Address
from .._models import BaseModel

__all__ = ["AddressGetResponse"]


class AddressGetResponse(BaseModel):
    data: Address
    """Physical address associated with a Terminal shop user."""
