# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .token import Token
from .._models import BaseModel

__all__ = ["TokenGetResponse"]


class TokenGetResponse(BaseModel):
    data: Token
    """A personal access token used to access the Terminal API.

    If you leak this, expect large sums of coffee to be ordered on your credit card.
    """
