# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["CardCollectResponse", "Data"]


class Data(BaseModel):
    url: str
    """
    Temporary URL that allows a user to enter credit card details over https at
    terminal.shop.
    """


class CardCollectResponse(BaseModel):
    data: Data
    """URL for collecting card information."""
