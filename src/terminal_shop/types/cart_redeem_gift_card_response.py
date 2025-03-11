# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CartRedeemGiftCardResponse", "Data"]


class Data(BaseModel):
    applied_amount: int = FieldInfo(alias="appliedAmount")

    gift_card_id: str = FieldInfo(alias="giftCardID")

    remaining_balance: int = FieldInfo(alias="remainingBalance")


class CartRedeemGiftCardResponse(BaseModel):
    data: Data
    """Gift card redemption result"""
