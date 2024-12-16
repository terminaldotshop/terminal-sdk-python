# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ProductVariant"]


class ProductVariant(BaseModel):
    id: str
    """Unique object identifier. The format and length of IDs may change over time."""

    name: str
    """Name of the product variant."""

    price: int
    """Price of the product variant in cents (USD)."""
