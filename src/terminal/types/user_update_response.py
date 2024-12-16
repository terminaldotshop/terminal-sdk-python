# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .shared.user import User

__all__ = ["UserUpdateResponse"]


class UserUpdateResponse(BaseModel):
    data: User
    """A Terminal shop user. (We have users, btw.)"""
