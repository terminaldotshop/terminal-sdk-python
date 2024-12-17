# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .app import App
from .._models import BaseModel

__all__ = ["AppGetResponse"]


class AppGetResponse(BaseModel):
    data: App
    """A Terminal App used for configuring an OAuth 2.0 client."""
