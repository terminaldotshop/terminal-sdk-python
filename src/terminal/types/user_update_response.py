# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .user import User
from .._models import BaseModel

__all__ = ["UserUpdateResponse"]


class UserUpdateResponse(BaseModel):
    data: User
    """A Terminal shop user. (We have users, btw.)"""
