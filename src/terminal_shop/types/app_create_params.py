# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AppCreateParams"]


class AppCreateParams(TypedDict, total=False):
    id: Required[str]
    """Unique object identifier. The format and length of IDs may change over time."""

    name: Required[str]
    """Name of the app."""

    redirect_uri: Required[Annotated[str, PropertyInfo(alias="redirectURI")]]
    """Redirect URI of the app."""
