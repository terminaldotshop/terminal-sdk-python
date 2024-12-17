# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["TokenCreateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Personal token ID."""

    token: str
    """Personal access token.

    Include this in the Authorization header (`Bearer <token>`) when accessing the
    Terminal API.
    """


class TokenCreateResponse(BaseModel):
    data: Data
