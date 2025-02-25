# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["App"]


class App(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    name: str
    """Name of the app."""

    redirect_uri: str = FieldInfo(alias="redirectURI")
    """Redirect URI of the app."""

    secret: str
    """OAuth 2.0 client secret of the app (obfuscated)."""
