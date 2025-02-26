# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import OrderGetResponse, OrderListResponse, OrderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Terminal) -> None:
        order = client.order.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Terminal) -> None:
        response = client.order.with_raw_response.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Terminal) -> None:
        with client.order.with_streaming_response.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCreateResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Terminal) -> None:
        order = client.order.list()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Terminal) -> None:
        response = client.order.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Terminal) -> None:
        with client.order.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Terminal) -> None:
        order = client.order.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(OrderGetResponse, order, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Terminal) -> None:
        response = client.order.with_raw_response.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderGetResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Terminal) -> None:
        with client.order.with_streaming_response.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderGetResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.order.with_raw_response.get(
                "",
            )


class TestAsyncOrder:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTerminal) -> None:
        order = await async_client.order.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTerminal) -> None:
        response = await async_client.order.with_raw_response.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTerminal) -> None:
        async with async_client.order.with_streaming_response.create(
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            variants={"var_XXXXXXXXXXXXXXXXXXXXXXXXX": 1},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCreateResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTerminal) -> None:
        order = await async_client.order.list()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTerminal) -> None:
        response = await async_client.order.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTerminal) -> None:
        async with async_client.order.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncTerminal) -> None:
        order = await async_client.order.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(OrderGetResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTerminal) -> None:
        response = await async_client.order.with_raw_response.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderGetResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTerminal) -> None:
        async with async_client.order.with_streaming_response.get(
            "ord_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderGetResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.order.with_raw_response.get(
                "",
            )
