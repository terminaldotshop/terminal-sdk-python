# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["CardCreateResponse"]


class CardCreateResponse(BaseModel):
    data: str
    """ID of the card."""
