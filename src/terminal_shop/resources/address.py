# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import address_create_params
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
from ..types.address_get_response import AddressGetResponse
from ..types.address_list_response import AddressListResponse
from ..types.address_create_response import AddressCreateResponse
from ..types.address_delete_response import AddressDeleteResponse

__all__ = ["AddressResource", "AsyncAddressResource"]


class AddressResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AddressResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        city: str,
        country: str,
        name: str,
        street1: str,
        zip: str,
        phone: str | NotGiven = NOT_GIVEN,
        province: str | NotGiven = NOT_GIVEN,
        street2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        Create and add a shipping address to the current user.

        Args:
          city: City of the address.

          country: ISO 3166-1 alpha-2 country code of the address.

          name: The recipient's name.

          street1: Street of the address.

          zip: Zip code of the address.

          phone: Phone number of the recipient.

          province: Province or state of the address.

          street2: Apartment, suite, etc. of the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/address",
            body=maybe_transform(
                {
                    "city": city,
                    "country": country,
                    "name": name,
                    "street1": street1,
                    "zip": zip,
                    "phone": phone,
                    "province": province,
                    "street2": street2,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
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
    ) -> AddressListResponse:
        """Get the shipping addresses associated with the current user."""
        return self._get(
            "/address",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressListResponse,
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
    ) -> AddressDeleteResponse:
        """
        Delete a shipping address from the current user.

        Args:
          id: ID of the shipping address to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/address/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
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
    ) -> AddressGetResponse:
        """
        Get the shipping address with the given ID.

        Args:
          id: ID of the shipping address to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/address/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressGetResponse,
        )


class AsyncAddressResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/terminaldotshop/terminal-sdk-python#with_streaming_response
        """
        return AsyncAddressResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        city: str,
        country: str,
        name: str,
        street1: str,
        zip: str,
        phone: str | NotGiven = NOT_GIVEN,
        province: str | NotGiven = NOT_GIVEN,
        street2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        Create and add a shipping address to the current user.

        Args:
          city: City of the address.

          country: ISO 3166-1 alpha-2 country code of the address.

          name: The recipient's name.

          street1: Street of the address.

          zip: Zip code of the address.

          phone: Phone number of the recipient.

          province: Province or state of the address.

          street2: Apartment, suite, etc. of the address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/address",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "country": country,
                    "name": name,
                    "street1": street1,
                    "zip": zip,
                    "phone": phone,
                    "province": province,
                    "street2": street2,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
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
    ) -> AddressListResponse:
        """Get the shipping addresses associated with the current user."""
        return await self._get(
            "/address",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressListResponse,
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
    ) -> AddressDeleteResponse:
        """
        Delete a shipping address from the current user.

        Args:
          id: ID of the shipping address to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/address/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
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
    ) -> AddressGetResponse:
        """
        Get the shipping address with the given ID.

        Args:
          id: ID of the shipping address to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/address/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressGetResponse,
        )


class AddressResourceWithRawResponse:
    def __init__(self, address: AddressResource) -> None:
        self._address = address

        self.create = to_raw_response_wrapper(
            address.create,
        )
        self.list = to_raw_response_wrapper(
            address.list,
        )
        self.delete = to_raw_response_wrapper(
            address.delete,
        )
        self.get = to_raw_response_wrapper(
            address.get,
        )


class AsyncAddressResourceWithRawResponse:
    def __init__(self, address: AsyncAddressResource) -> None:
        self._address = address

        self.create = async_to_raw_response_wrapper(
            address.create,
        )
        self.list = async_to_raw_response_wrapper(
            address.list,
        )
        self.delete = async_to_raw_response_wrapper(
            address.delete,
        )
        self.get = async_to_raw_response_wrapper(
            address.get,
        )


class AddressResourceWithStreamingResponse:
    def __init__(self, address: AddressResource) -> None:
        self._address = address

        self.create = to_streamed_response_wrapper(
            address.create,
        )
        self.list = to_streamed_response_wrapper(
            address.list,
        )
        self.delete = to_streamed_response_wrapper(
            address.delete,
        )
        self.get = to_streamed_response_wrapper(
            address.get,
        )


class AsyncAddressResourceWithStreamingResponse:
    def __init__(self, address: AsyncAddressResource) -> None:
        self._address = address

        self.create = async_to_streamed_response_wrapper(
            address.create,
        )
        self.list = async_to_streamed_response_wrapper(
            address.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            address.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            address.get,
        )
