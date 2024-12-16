# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["AddressCreateResponse"]


class AddressCreateResponse(BaseModel):
    data: str
    """Shipping address ID."""
