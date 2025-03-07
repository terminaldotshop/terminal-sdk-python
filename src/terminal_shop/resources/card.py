# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import card_create_params
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
from ..types.card_get_response import CardGetResponse
from ..types.card_list_response import CardListResponse
from ..types.card_create_response import CardCreateResponse
from ..types.card_delete_response import CardDeleteResponse
from ..types.card_collect_response import CardCollectResponse

__all__ = ["CardResource", "AsyncCardResource"]


class CardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return CardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCreateResponse:
        """
        Attach a credit card (tokenized via Stripe) to the current user.

        Args:
          token: Stripe card token. Learn how to
              [create one here](https://docs.stripe.com/api/tokens/create_card).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/card",
            body=maybe_transform({"token": token}, card_create_params.CardCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardListResponse:
        """List the credit cards associated with the current user."""
        return self._get(
            "/card",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDeleteResponse:
        """
        Delete a credit card associated with the current user.

        Args:
          id: ID of the card to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/card/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDeleteResponse,
        )

    def collect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCollectResponse:
        """
        Create a temporary URL for collecting credit card information for the current
        user.
        """
        return self._post(
            "/card/collect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCollectResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardGetResponse:
        """
        Get a credit card by ID associated with the current user.

        Args:
          id: ID of the card to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/card/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardGetResponse,
        )


class AsyncCardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncCardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCreateResponse:
        """
        Attach a credit card (tokenized via Stripe) to the current user.

        Args:
          token: Stripe card token. Learn how to
              [create one here](https://docs.stripe.com/api/tokens/create_card).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/card",
            body=await async_maybe_transform({"token": token}, card_create_params.CardCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCreateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardListResponse:
        """List the credit cards associated with the current user."""
        return await self._get(
            "/card",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardDeleteResponse:
        """
        Delete a credit card associated with the current user.

        Args:
          id: ID of the card to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/card/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardDeleteResponse,
        )

    async def collect(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardCollectResponse:
        """
        Create a temporary URL for collecting credit card information for the current
        user.
        """
        return await self._post(
            "/card/collect",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardCollectResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardGetResponse:
        """
        Get a credit card by ID associated with the current user.

        Args:
          id: ID of the card to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/card/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardGetResponse,
        )


class CardResourceWithRawResponse:
    def __init__(self, card: CardResource) -> None:
        self._card = card

        self.create = to_raw_response_wrapper(
            card.create,
        )
        self.list = to_raw_response_wrapper(
            card.list,
        )
        self.delete = to_raw_response_wrapper(
            card.delete,
        )
        self.collect = to_raw_response_wrapper(
            card.collect,
        )
        self.get = to_raw_response_wrapper(
            card.get,
        )


class AsyncCardResourceWithRawResponse:
    def __init__(self, card: AsyncCardResource) -> None:
        self._card = card

        self.create = async_to_raw_response_wrapper(
            card.create,
        )
        self.list = async_to_raw_response_wrapper(
            card.list,
        )
        self.delete = async_to_raw_response_wrapper(
            card.delete,
        )
        self.collect = async_to_raw_response_wrapper(
            card.collect,
        )
        self.get = async_to_raw_response_wrapper(
            card.get,
        )


class CardResourceWithStreamingResponse:
    def __init__(self, card: CardResource) -> None:
        self._card = card

        self.create = to_streamed_response_wrapper(
            card.create,
        )
        self.list = to_streamed_response_wrapper(
            card.list,
        )
        self.delete = to_streamed_response_wrapper(
            card.delete,
        )
        self.collect = to_streamed_response_wrapper(
            card.collect,
        )
        self.get = to_streamed_response_wrapper(
            card.get,
        )


class AsyncCardResourceWithStreamingResponse:
    def __init__(self, card: AsyncCardResource) -> None:
        self._card = card

        self.create = async_to_streamed_response_wrapper(
            card.create,
        )
        self.list = async_to_streamed_response_wrapper(
            card.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            card.delete,
        )
        self.collect = async_to_streamed_response_wrapper(
            card.collect,
        )
        self.get = async_to_streamed_response_wrapper(
            card.get,
        )
