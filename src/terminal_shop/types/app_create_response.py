# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["AppCreateResponse", "Data"]


class Data(BaseModel):
    id: str
    """OAuth 2.0 client ID."""

    secret: str
    """OAuth 2.0 client secret."""


class AppCreateResponse(BaseModel):
    data: Data
