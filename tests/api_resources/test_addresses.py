# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from terminal import Terminal, AsyncTerminal
from tests.utils import assert_matches_type
from terminal.types import AddressListResponse, AddressCreateResponse, AddressDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Terminal) -> None:
        address = client.addresses.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Terminal) -> None:
        address = client.addresses.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
            phone="5555555555",
            province="CA",
            street2="Apt 1",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Terminal) -> None:
        response = client.addresses.with_raw_response.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Terminal) -> None:
        with client.addresses.with_streaming_response.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Terminal) -> None:
        address = client.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Terminal) -> None:
        response = client.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Terminal) -> None:
        with client.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Terminal) -> None:
        address = client.addresses.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Terminal) -> None:
        response = client.addresses.with_raw_response.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Terminal) -> None:
        with client.addresses.with_streaming_response.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.addresses.with_raw_response.delete(
                "",
            )


class TestAsyncAddresses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTerminal) -> None:
        address = await async_client.addresses.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTerminal) -> None:
        address = await async_client.addresses.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
            phone="5555555555",
            province="CA",
            street2="Apt 1",
        )
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTerminal) -> None:
        response = await async_client.addresses.with_raw_response.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressCreateResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTerminal) -> None:
        async with async_client.addresses.with_streaming_response.create(
            city="Anytown",
            country="US",
            name="John Doe",
            street1="123 Main St",
            zip="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressCreateResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTerminal) -> None:
        address = await async_client.addresses.list()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTerminal) -> None:
        response = await async_client.addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressListResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTerminal) -> None:
        async with async_client.addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressListResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTerminal) -> None:
        address = await async_client.addresses.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTerminal) -> None:
        response = await async_client.addresses.with_raw_response.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTerminal) -> None:
        async with async_client.addresses.with_streaming_response.delete(
            "shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.addresses.with_raw_response.delete(
                "",
            )
