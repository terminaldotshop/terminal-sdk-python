# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .profile import Profile
from .._models import BaseModel

__all__ = ["ProfileUpdateResponse"]


class ProfileUpdateResponse(BaseModel):
    data: Profile
    """A Terminal shop user's profile. (We have users, btw.)"""
