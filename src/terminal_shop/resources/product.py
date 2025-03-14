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
from ..types.product_get_response import ProductGetResponse
from ..types.product_list_response import ProductListResponse

__all__ = ["ProductResource", "AsyncProductResource"]


class ProductResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return ProductResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductListResponse:
        """List all products for sale in the Terminal shop."""
        return self._get(
            "/product",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
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
    ) -> ProductGetResponse:
        """
        Get a product by ID from the Terminal shop.

        Args:
          id: ID of the product to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/product/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductGetResponse,
        )


class AsyncProductResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncProductResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductListResponse:
        """List all products for sale in the Terminal shop."""
        return await self._get(
            "/product",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListResponse,
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
    ) -> ProductGetResponse:
        """
        Get a product by ID from the Terminal shop.

        Args:
          id: ID of the product to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/product/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductGetResponse,
        )


class ProductResourceWithRawResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

        self.list = to_raw_response_wrapper(
            product.list,
        )
        self.get = to_raw_response_wrapper(
            product.get,
        )


class AsyncProductResourceWithRawResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

        self.list = async_to_raw_response_wrapper(
            product.list,
        )
        self.get = async_to_raw_response_wrapper(
            product.get,
        )


class ProductResourceWithStreamingResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

        self.list = to_streamed_response_wrapper(
            product.list,
        )
        self.get = to_streamed_response_wrapper(
            product.get,
        )


class AsyncProductResourceWithStreamingResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

        self.list = async_to_streamed_response_wrapper(
            product.list,
        )
        self.get = async_to_streamed_response_wrapper(
            product.get,
        )
