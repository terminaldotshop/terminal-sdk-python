# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import cart_set_card_params, cart_set_item_params, cart_set_address_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.cart_get_response import CartGetResponse
from ..types.cart_clear_response import CartClearResponse
from ..types.cart_convert_response import CartConvertResponse
from ..types.cart_set_card_response import CartSetCardResponse
from ..types.cart_set_item_response import CartSetItemResponse
from ..types.cart_set_address_response import CartSetAddressResponse

__all__ = ["CartResource", "AsyncCartResource"]


class CartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return CartResourceWithStreamingResponse(self)

    def clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartClearResponse:
        """Clear the current user's cart."""
        return self._delete(
            "/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartClearResponse,
        )

    def convert(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartConvertResponse:
        """Convert the current user's cart to an order."""
        return self._post(
            "/cart/convert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartConvertResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartGetResponse:
        """Get the current user's cart."""
        return self._get(
            "/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartGetResponse,
        )

    def set_address(
        self,
        *,
        address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetAddressResponse:
        """
        Set the shipping address for the current user's cart.

        Args:
          address_id: ID of the shipping address to set for the current user's cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/cart/address",
            body=maybe_transform({"address_id": address_id}, cart_set_address_params.CartSetAddressParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetAddressResponse,
        )

    def set_card(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetCardResponse:
        """
        Set the credit card for the current user's cart.

        Args:
          card_id: ID of the credit card to set for the current user's cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/cart/card",
            body=maybe_transform({"card_id": card_id}, cart_set_card_params.CartSetCardParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetCardResponse,
        )

    def set_item(
        self,
        *,
        product_variant_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetItemResponse:
        """
        Add an item to the current user's cart.

        Args:
          product_variant_id: ID of the product variant to add to the cart.

          quantity: Quantity of the item to add to the cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/cart/item",
            body=maybe_transform(
                {
                    "product_variant_id": product_variant_id,
                    "quantity": quantity,
                },
                cart_set_item_params.CartSetItemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetItemResponse,
        )


class AsyncCartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncCartResourceWithStreamingResponse(self)

    async def clear(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartClearResponse:
        """Clear the current user's cart."""
        return await self._delete(
            "/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartClearResponse,
        )

    async def convert(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartConvertResponse:
        """Convert the current user's cart to an order."""
        return await self._post(
            "/cart/convert",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartConvertResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartGetResponse:
        """Get the current user's cart."""
        return await self._get(
            "/cart",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartGetResponse,
        )

    async def set_address(
        self,
        *,
        address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetAddressResponse:
        """
        Set the shipping address for the current user's cart.

        Args:
          address_id: ID of the shipping address to set for the current user's cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/cart/address",
            body=await async_maybe_transform({"address_id": address_id}, cart_set_address_params.CartSetAddressParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetAddressResponse,
        )

    async def set_card(
        self,
        *,
        card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetCardResponse:
        """
        Set the credit card for the current user's cart.

        Args:
          card_id: ID of the credit card to set for the current user's cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/cart/card",
            body=await async_maybe_transform({"card_id": card_id}, cart_set_card_params.CartSetCardParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetCardResponse,
        )

    async def set_item(
        self,
        *,
        product_variant_id: str,
        quantity: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CartSetItemResponse:
        """
        Add an item to the current user's cart.

        Args:
          product_variant_id: ID of the product variant to add to the cart.

          quantity: Quantity of the item to add to the cart.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/cart/item",
            body=await async_maybe_transform(
                {
                    "product_variant_id": product_variant_id,
                    "quantity": quantity,
                },
                cart_set_item_params.CartSetItemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CartSetItemResponse,
        )


class CartResourceWithRawResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.clear = to_raw_response_wrapper(
            cart.clear,
        )
        self.convert = to_raw_response_wrapper(
            cart.convert,
        )
        self.get = to_raw_response_wrapper(
            cart.get,
        )
        self.set_address = to_raw_response_wrapper(
            cart.set_address,
        )
        self.set_card = to_raw_response_wrapper(
            cart.set_card,
        )
        self.set_item = to_raw_response_wrapper(
            cart.set_item,
        )


class AsyncCartResourceWithRawResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.clear = async_to_raw_response_wrapper(
            cart.clear,
        )
        self.convert = async_to_raw_response_wrapper(
            cart.convert,
        )
        self.get = async_to_raw_response_wrapper(
            cart.get,
        )
        self.set_address = async_to_raw_response_wrapper(
            cart.set_address,
        )
        self.set_card = async_to_raw_response_wrapper(
            cart.set_card,
        )
        self.set_item = async_to_raw_response_wrapper(
            cart.set_item,
        )


class CartResourceWithStreamingResponse:
    def __init__(self, cart: CartResource) -> None:
        self._cart = cart

        self.clear = to_streamed_response_wrapper(
            cart.clear,
        )
        self.convert = to_streamed_response_wrapper(
            cart.convert,
        )
        self.get = to_streamed_response_wrapper(
            cart.get,
        )
        self.set_address = to_streamed_response_wrapper(
            cart.set_address,
        )
        self.set_card = to_streamed_response_wrapper(
            cart.set_card,
        )
        self.set_item = to_streamed_response_wrapper(
            cart.set_item,
        )


class AsyncCartResourceWithStreamingResponse:
    def __init__(self, cart: AsyncCartResource) -> None:
        self._cart = cart

        self.clear = async_to_streamed_response_wrapper(
            cart.clear,
        )
        self.convert = async_to_streamed_response_wrapper(
            cart.convert,
        )
        self.get = async_to_streamed_response_wrapper(
            cart.get,
        )
        self.set_address = async_to_streamed_response_wrapper(
            cart.set_address,
        )
        self.set_card = async_to_streamed_response_wrapper(
            cart.set_card,
        )
        self.set_item = async_to_streamed_response_wrapper(
            cart.set_item,
        )
