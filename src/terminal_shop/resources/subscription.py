# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import subscription_create_params, subscription_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.subscription_get_response import SubscriptionGetResponse
from ..types.subscription_list_response import SubscriptionListResponse
from ..types.subscription_create_response import SubscriptionCreateResponse
from ..types.subscription_delete_response import SubscriptionDeleteResponse
from ..types.subscription_update_response import SubscriptionUpdateResponse

__all__ = ["SubscriptionResource", "AsyncSubscriptionResource"]


class SubscriptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return SubscriptionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        address_id: str,
        card_id: str,
        created: str,
        price: int,
        product_variant_id: str,
        quantity: int,
        next: str | Omit = omit,
        schedule: subscription_create_params.Schedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Create a subscription for the current user.

        Args:
          id: Unique object identifier. The format and length of IDs may change over time.

          address_id: ID of the shipping address used for the subscription.

          card_id: ID of the card used for the subscription.

          created: Date the subscription was created.

          price: Price of the subscription in cents (USD).

          product_variant_id: ID of the product variant being subscribed to.

          quantity: Quantity of the subscription.

          next: Next shipment and billing date for the subscription.

          schedule: Schedule of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/subscription",
            body=maybe_transform(
                {
                    "id": id,
                    "address_id": address_id,
                    "card_id": card_id,
                    "created": created,
                    "price": price,
                    "product_variant_id": product_variant_id,
                    "quantity": quantity,
                    "next": next,
                    "schedule": schedule,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        address_id: str | Omit = omit,
        card_id: str | Omit = omit,
        schedule: subscription_update_params.Schedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdateResponse:
        """
        Update card, address, or interval for an existing subscription.

        Args:
          id: ID of the subscription to update.

          address_id: New shipping address ID for the subscription.

          card_id: New payment method ID for the subscription.

          schedule: New schedule for the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/subscription/{id}",
            body=maybe_transform(
                {
                    "address_id": address_id,
                    "card_id": card_id,
                    "schedule": schedule,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """List the subscriptions associated with the current user."""
        return self._get(
            "/subscription",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDeleteResponse:
        """
        Cancel a subscription for the current user.

        Args:
          id: ID of the subscription to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/subscription/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionGetResponse:
        """
        Get the subscription with the given ID.

        Args:
          id: ID of the subscription to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/subscription/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionGetResponse,
        )


class AsyncSubscriptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncSubscriptionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        address_id: str,
        card_id: str,
        created: str,
        price: int,
        product_variant_id: str,
        quantity: int,
        next: str | Omit = omit,
        schedule: subscription_create_params.Schedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Create a subscription for the current user.

        Args:
          id: Unique object identifier. The format and length of IDs may change over time.

          address_id: ID of the shipping address used for the subscription.

          card_id: ID of the card used for the subscription.

          created: Date the subscription was created.

          price: Price of the subscription in cents (USD).

          product_variant_id: ID of the product variant being subscribed to.

          quantity: Quantity of the subscription.

          next: Next shipment and billing date for the subscription.

          schedule: Schedule of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/subscription",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "address_id": address_id,
                    "card_id": card_id,
                    "created": created,
                    "price": price,
                    "product_variant_id": product_variant_id,
                    "quantity": quantity,
                    "next": next,
                    "schedule": schedule,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        address_id: str | Omit = omit,
        card_id: str | Omit = omit,
        schedule: subscription_update_params.Schedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdateResponse:
        """
        Update card, address, or interval for an existing subscription.

        Args:
          id: ID of the subscription to update.

          address_id: New shipping address ID for the subscription.

          card_id: New payment method ID for the subscription.

          schedule: New schedule for the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/subscription/{id}",
            body=await async_maybe_transform(
                {
                    "address_id": address_id,
                    "card_id": card_id,
                    "schedule": schedule,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """List the subscriptions associated with the current user."""
        return await self._get(
            "/subscription",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDeleteResponse:
        """
        Cancel a subscription for the current user.

        Args:
          id: ID of the subscription to cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/subscription/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDeleteResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionGetResponse:
        """
        Get the subscription with the given ID.

        Args:
          id: ID of the subscription to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/subscription/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionGetResponse,
        )


class SubscriptionResourceWithRawResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.create = to_raw_response_wrapper(
            subscription.create,
        )
        self.update = to_raw_response_wrapper(
            subscription.update,
        )
        self.list = to_raw_response_wrapper(
            subscription.list,
        )
        self.delete = to_raw_response_wrapper(
            subscription.delete,
        )
        self.get = to_raw_response_wrapper(
            subscription.get,
        )


class AsyncSubscriptionResourceWithRawResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.create = async_to_raw_response_wrapper(
            subscription.create,
        )
        self.update = async_to_raw_response_wrapper(
            subscription.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscription.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscription.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subscription.get,
        )


class SubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.create = to_streamed_response_wrapper(
            subscription.create,
        )
        self.update = to_streamed_response_wrapper(
            subscription.update,
        )
        self.list = to_streamed_response_wrapper(
            subscription.list,
        )
        self.delete = to_streamed_response_wrapper(
            subscription.delete,
        )
        self.get = to_streamed_response_wrapper(
            subscription.get,
        )


class AsyncSubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.create = async_to_streamed_response_wrapper(
            subscription.create,
        )
        self.update = async_to_streamed_response_wrapper(
            subscription.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscription.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscription.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subscription.get,
        )
