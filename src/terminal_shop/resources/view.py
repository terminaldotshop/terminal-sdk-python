# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.view_init_response import ViewInitResponse

__all__ = ["ViewResource", "AsyncViewResource"]


class ViewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return ViewResourceWithStreamingResponse(self)

    def init(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ViewInitResponse:
        """
        Get initial app data, including user, products, cart, addresses, cards,
        subscriptions, and orders.
        """
        return self._get(
            "/view/init",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewInitResponse,
        )


class AsyncViewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncViewResourceWithStreamingResponse(self)

    async def init(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ViewInitResponse:
        """
        Get initial app data, including user, products, cart, addresses, cards,
        subscriptions, and orders.
        """
        return await self._get(
            "/view/init",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ViewInitResponse,
        )


class ViewResourceWithRawResponse:
    def __init__(self, view: ViewResource) -> None:
        self._view = view

        self.init = to_raw_response_wrapper(
            view.init,
        )


class AsyncViewResourceWithRawResponse:
    def __init__(self, view: AsyncViewResource) -> None:
        self._view = view

        self.init = async_to_raw_response_wrapper(
            view.init,
        )


class ViewResourceWithStreamingResponse:
    def __init__(self, view: ViewResource) -> None:
        self._view = view

        self.init = to_streamed_response_wrapper(
            view.init,
        )


class AsyncViewResourceWithStreamingResponse:
    def __init__(self, view: AsyncViewResource) -> None:
        self._view = view

        self.init = async_to_streamed_response_wrapper(
            view.init,
        )
