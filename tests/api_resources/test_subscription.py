# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from terminal_shop import Terminal, AsyncTerminal
from terminal_shop.types import (
    SubscriptionGetResponse,
    SubscriptionListResponse,
    SubscriptionCreateResponse,
    SubscriptionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Terminal) -> None:
        subscription = client.subscription.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Terminal) -> None:
        subscription = client.subscription.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
            next="2025-02-01T19:36:19.000Z",
            schedule={
                "interval": 3,
                "type": "weekly",
            },
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Terminal) -> None:
        response = client.subscription.with_raw_response.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Terminal) -> None:
        with client.subscription.with_streaming_response.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Terminal) -> None:
        subscription = client.subscription.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Terminal) -> None:
        response = client.subscription.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Terminal) -> None:
        with client.subscription.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Terminal) -> None:
        subscription = client.subscription.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Terminal) -> None:
        response = client.subscription.with_raw_response.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Terminal) -> None:
        with client.subscription.with_streaming_response.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.subscription.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Terminal) -> None:
        subscription = client.subscription.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Terminal) -> None:
        response = client.subscription.with_raw_response.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Terminal) -> None:
        with client.subscription.with_streaming_response.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Terminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.subscription.with_raw_response.get(
                "",
            )


class TestAsyncSubscription:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTerminal) -> None:
        subscription = await async_client.subscription.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTerminal) -> None:
        subscription = await async_client.subscription.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
            next="2025-02-01T19:36:19.000Z",
            schedule={
                "interval": 3,
                "type": "weekly",
            },
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTerminal) -> None:
        response = await async_client.subscription.with_raw_response.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTerminal) -> None:
        async with async_client.subscription.with_streaming_response.create(
            id="sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
            address_id="shp_XXXXXXXXXXXXXXXXXXXXXXXXX",
            card_id="crd_XXXXXXXXXXXXXXXXXXXXXXXXX",
            product_variant_id="var_XXXXXXXXXXXXXXXXXXXXXXXXX",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTerminal) -> None:
        subscription = await async_client.subscription.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTerminal) -> None:
        response = await async_client.subscription.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTerminal) -> None:
        async with async_client.subscription.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTerminal) -> None:
        subscription = await async_client.subscription.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTerminal) -> None:
        response = await async_client.subscription.with_raw_response.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTerminal) -> None:
        async with async_client.subscription.with_streaming_response.delete(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.subscription.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncTerminal) -> None:
        subscription = await async_client.subscription.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncTerminal) -> None:
        response = await async_client.subscription.with_raw_response.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncTerminal) -> None:
        async with async_client.subscription.with_streaming_response.get(
            "sub_XXXXXXXXXXXXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncTerminal) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.subscription.with_raw_response.get(
                "",
            )
