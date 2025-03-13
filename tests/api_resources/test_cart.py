# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import (
    CartGetResponse,
    CartClearResponse,
    CartConvertResponse,
    CartSetCardResponse,
    CartSetItemResponse,
    CartSetAddressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_clear(self, client: Terminal) -> None:
        cart = client.cart.clear()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_clear(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_clear(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartClearResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_convert(self, client: Terminal) -> None:
        cart = client.cart.convert()
        assert_matches_type(CartConvertResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.convert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartConvertResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.convert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartConvertResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Terminal) -> None:
        cart = client.cart.get()
        assert_matches_type(CartGetResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartGetResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartGetResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_address(self, client: Terminal) -> None:
        cart = client.cart.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CartSetAddressResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_set_address(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartSetAddressResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_set_address(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartSetAddressResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_card(self, client: Terminal) -> None:
        cart = client.cart.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CartSetCardResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_set_card(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartSetCardResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_set_card(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartSetCardResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_item(self, client: Terminal) -> None:
        cart = client.cart.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        )
        assert_matches_type(CartSetItemResponse, cart, path=["response"])

    @parametrize
    def test_raw_response_set_item(self, client: Terminal) -> None:
        response = client.cart.with_raw_response.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = response.parse()
        assert_matches_type(CartSetItemResponse, cart, path=["response"])

    @parametrize
    def test_streaming_response_set_item(self, client: Terminal) -> None:
        with client.cart.with_streaming_response.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = response.parse()
            assert_matches_type(CartSetItemResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCart:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_clear(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.clear()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartClearResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartClearResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_convert(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.convert()
        assert_matches_type(CartConvertResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.convert()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartConvertResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.convert() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartConvertResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.get()
        assert_matches_type(CartGetResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartGetResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartGetResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_address(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CartSetAddressResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_set_address(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartSetAddressResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_set_address(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.set_address(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartSetAddressResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_card(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(CartSetCardResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_set_card(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartSetCardResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_set_card(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.set_card(
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartSetCardResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_item(self, async_client: AsyncTerminal) -> None:
        cart = await async_client.cart.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        )
        assert_matches_type(CartSetItemResponse, cart, path=["response"])

    @parametrize
    async def test_raw_response_set_item(self, async_client: AsyncTerminal) -> None:
        response = await async_client.cart.with_raw_response.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cart = await response.parse()
        assert_matches_type(CartSetItemResponse, cart, path=["response"])

    @parametrize
    async def test_streaming_response_set_item(self, async_client: AsyncTerminal) -> None:
        async with async_client.cart.with_streaming_response.set_item(
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=2,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cart = await response.parse()
            assert_matches_type(CartSetItemResponse, cart, path=["response"])

        assert cast(Any, response.is_closed) is True
