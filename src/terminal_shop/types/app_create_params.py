# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppCreateParams"]


class AppCreateParams(TypedDict, total=False):
    name: Required[str]

    redirect_uri: Required[Annotated[str, PropertyInfo(alias="redirectURI")]]
